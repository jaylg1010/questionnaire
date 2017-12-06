from django.shortcuts import render,HttpResponse
from app01 import models
from django.forms import Form
from django.forms import fields
from django.forms import widgets

# Create your views here.


def login(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=models.UserInfo.objects.filter(username=username,password=password)
    stu=models.Student.objects.filter(username=username,password=password)
    if user:
        questionnaire_list=models.Questionnaire.objects.all()
        return render(request,"Userinfo_Index.html",{"questionnaire_list":questionnaire_list})
    elif stu:
        return render(request,"Student_Index.html")
    else:
        return render(request,"login.html")


"""
新建form表单，有问题，类型字段，前端根据类型显示不同的样式
"""

class Edit_questionnaire_Form(Form):
    question = fields.CharField(
        required=True,
        error_messages={
            'required':'问题不能为空',
        },
        widget=widgets.Textarea(attrs={"style":"width:600px;height:50px"})
    )

    type = fields.ChoiceField(
        choices=((1,'单选'),(2,'打分(0-10分)'),(3,'建议')),
        required=True,
        error_messages={
            'required':'类型不能为空'
        },
        widget=widgets.Select(attrs={"style":"width:200px;height:25px"})
    )


def edit_questionnaire(request,questionnaire_id):
    """
    利用form表单，实现编辑问题
    如果没有问题，实力一个默认的form表单
    如果有问题，找到所有的问题，实例form表单，传到前端
    :param question:
    :return:
    """
    # 查找这个问卷是否有问题
    questionnaire_obj=models.Questionnaire.objects.filter(id=questionnaire_id).first()
    question_caption=questionnaire_obj.question_set.all()
    print(question_caption)
    if request.method=="POST":
        pass
    else:
        if question_caption:
            # 如果有问题，循环问题form实例化每个表单
            question_l=[]
            for question_obj in question_caption:
                question_form=Edit_questionnaire_Form(initial={"question":question_obj.caption,"type":question_obj.type})
                question_l.append(question_form)
            return render(request,"Edit_Questionnaire.html",{"question_l":question_l})
        else:
            # 如果没有问题，就只实例一个form表单
            question_form=Edit_questionnaire_Form()
            return render(request,"Edit_Questionnaire.html",{"question_form":question_form})