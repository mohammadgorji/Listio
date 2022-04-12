from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def home(request):
	return render(request, "todo/home.html", {})

def about(request):
	return render(request, "todo/about.html", {})

@login_required
def todolist(request, id):
	ls = ToDoList.objects.get(pk=id)
	
	if ls in request.user.todolist.all():
		if request.method == "POST":
			if request.POST.get("save"):
				for item in ls.item_set.all():
					item.text = request.POST.get("t" + str(item.id))
					item.date_added = request.POST.get("d" + str(item.id))
					item.priority = request.POST.get("p" + str(item.id))
					if request.POST.get("c" + str(item.id)) == "clicked":
						item.complete = True
					else:
						item.complete = False
					item.save()

			elif request.POST.get("delete"):
				list_name = ls.name
				ls.delete()
				messages.success(request, '%s has been deleted from the existing lists!'%list_name)
				return redirect("/view/")

			elif request.POST.get("newItem"):
				txt = request.POST.get("new")
				priority = request.POST.get("priority")
				ls.item_set.create(text=txt,priority=priority, complete=False)

		return render(request, "todo/list.html", {"ls":ls})

	return render(request, "todo/home.html", {})

@login_required
def delete(request, list_id):
	item = Item.objects.get(pk=list_id)
	list_pk = item.todolist.id
	item.delete()
	messages.success(request, 'Item has been deleted from the List!')
	return redirect("/list/%i" %list_pk)

@login_required
def create(request):
	if request.method == "POST":
		form = CreateNewList(request.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]
			t = ToDoList(name=n)
			t.save()
			request.user.todolist.add(t)

		return HttpResponseRedirect("/list/%i" %t.id)

	else:
		form = CreateNewList()

	return render(request, "todo/create.html", {"form":form})

@login_required
def view(request):
	return render(request, "todo/view.html", {})