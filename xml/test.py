#!/user/bin.python
# -*- coding: UTF-8 -*-
import os
from xml.dom.minidom import parse
import xml.dom.minidom
import pandas as pd

def getAttributeData(element,attribute_name):
	if element.hasAttribute(attribute_name):
		attribute_value = element.getAttribute(attribute_name)
		# print(f"{attribute_name}:{attribute_value}")
		return attribute_value
	return None
def getElementsDataByTagName(element,tagName):
	element = element.getElementsByTagName(tagName)[0]
	element_value = element.childNodes[0].data
	# print(f'''{tagName}:{element_value}''')
	return element_value
# def getElementstreeByTagName(elementtree,tagNametree):
# 	elementtree = elementtree.getElementsByTagName(tagNametree)[0]
# 	return elementtree

def get_issue_report_dict(item,issuedict):

	# for x in get_element_data_list:
	# 	element_name = getElementstreeByTagName(item, x)
	# 	locals()[x] = element_name

	# issuedict = dict()
	title = getElementsDataByTagName(item, "title")
	if len(item.getElementsByTagName('description')) > 0:
		description = getElementsDataByTagName(item, "description")
		issuedict["description"] = description
	if len(item.getElementsByTagName('key')) > 0:
		key = item.getElementsByTagName('key')[0]
		key_name = key.childNodes[0].data
		key_name = key_name.split('-')
		# print(key_name[1])
		key_id = getAttributeData(key, "id")
		issuedict["issue_id"] = key_name[1]
		issuedict["key_id"] = key_id
	if len(item.getElementsByTagName('summary')) > 0:
		summary = item.getElementsByTagName('summary')[0]
		issuedict["summary"] = summary.childNodes[0].data
	if len(item.getElementsByTagName('status')) > 0:
		status = item.getElementsByTagName('status')[0]
		issuedict["status"] = status.childNodes[0].data
	if len(item.getElementsByTagName('resolution')) > 0:
		resolution = item.getElementsByTagName('resolution')[0]
		issuedict["resolution"] = resolution.childNodes[0].data
	if len(item.getElementsByTagName('created')) > 0:
		created = item.getElementsByTagName('created')[0]
		issuedict["created"] = created.childNodes[0].data
	if len(item.getElementsByTagName('updated')) > 0:
		updated = item.getElementsByTagName('updated')[0]
		issuedict["updated"] = updated.childNodes[0].data
	if len(item.getElementsByTagName('resolved')) > 0:
	# if item.getElementsByTagName("resolved") is not None:
		resolved = item.getElementsByTagName('resolved')[0]
		issuedict["resolved"] = resolved.childNodes[0].data
	if len(item.getElementsByTagName('version')) > 0:
		version = item.getElementsByTagName('version')[0]
		issuedict["version"] = version.childNodes[0].data
	if len(item.getElementsByTagName('project')) > 0:
		project = item.getElementsByTagName('project')[0]
		project_data = getElementsDataByTagName(item, "project")
		project_id = getAttributeData(project, "id")
		project_key = getAttributeData(project, "key")
		issuedict["project_data"] = project_data
		issuedict["project_id"] = project_id
		issuedict["project_name"] = project_key
	# key_name = key.childNodes[0].data
	# key_name = key_name.split('-')
	# print(key_name[1])
	# key_id = getAttributeData(key, "id")
	# issuedict["issue_id"] = key_name[1]
	# issuedict["key_id"] = key_id
	# issuedict["description"] = description.childNodes[0].data
	# issuedict["summary"] = summary.childNodes[0].data
	if len(item.getElementsByTagName('type')) > 0:
		type = item.getElementsByTagName('type')[0]
		type_data = getElementsDataByTagName(item, "type")
		type_id = getAttributeData(type, "id")
		type_iconUrl = getAttributeData(type, "iconUrl")
		issuedict["type_data"] = type_data
		issuedict["type_id"] = type_id
		issuedict["type_iconUrl"] = type_iconUrl
	if len(item.getElementsByTagName('priority')) > 0:
		priority = item.getElementsByTagName('priority')[0]
		priority_data = getElementsDataByTagName(item, "priority")
		priority_id = getAttributeData(priority, "id")
		priority_iconUrl = getAttributeData(priority, "iconUrl")
		# prioritydict = dict()
		issuedict["priority_data"] = priority_data
		issuedict["priority_id"] = priority_id
		issuedict["priority_iconUrl"] = priority_iconUrl
	# issuedict["status"] = status.childNodes[0].data
	# issuedict["resolution"] = resolution.childNodes[0].data
	if len(item.getElementsByTagName('assignee')) > 0:
		assignee = item.getElementsByTagName('assignee')[0]
		assignee_data = getElementsDataByTagName(item, "assignee")
		assignee_username = getAttributeData(assignee, "username")
		issuedict["assignee_data"] = assignee_data
		issuedict["assignee_username"] = assignee_username
	if len(item.getElementsByTagName('reporter')) > 0:
		reporter = item.getElementsByTagName('reporter')[0]
		reporter_data = getElementsDataByTagName(item, "reporter")
		reporter_username = getAttributeData(reporter, "username")
		issuedict["reporter_data"] = reporter_data
		issuedict["reporter_username"] = reporter_username
	# issuedict["created"] = created.childNodes[0].data
	# issuedict["updated"] = updated.childNodes[0].data
	# issuedict["resolved"] = resolved.childNodes[0].data
	# issuedict["version"] = version.childNodes[0].data
	return issuedict
def get_file_path(root_path,file_list,dir_list):
	dir_or_files = os.listdir(root_path)
	for dir_file in dir_or_files:
		dir_file_path = os.path.join(root_path,dir_file)
		if os.path.isdir(dir_file_path):
			dir_list.append(dir_file_path)
			get_file_path(dir_file_path,file_list,dir_list)
		else:
			file_list.append(dir_file_path)

# get_element_data_list = ['project', 'title','key','description', 'summary','type','key','priority','status','resolution','resolved','assignee','reporter','created','updated','version']
root_path = r"/Users/andiehuang/LCH/xml/"
file_list = []
dir_list = []
get_file_path(root_path,file_list,dir_list)
print(file_list)
print (dir_list)
def gread_all_xml(file_list):
	result = pd.DataFrame()
	for xml_file in file_list:
		if xml_file.endswith("xml"):
			DOMTree = xml.dom.minidom.parse(xml_file)
			rss = DOMTree.documentElement
			channel = rss.getElementsByTagName('channel')[0]
			item = channel.getElementsByTagName("item")[0]
			issuedict = dict()
			# get_element_data_list = ['project', 'title','key','description', 'summary','type','key','priority','status','resolution','resolved','assignee','reporter','created','updated','version']
			issuedict = get_issue_report_dict(item,issuedict)
			comments = item.getElementsByTagName("comments")[0]
			commentgroup = comments.getElementsByTagName("comment")
			comment_list = list()
			for comment in commentgroup:
				comment_dict = dict()
				comment_dict["comment_id"] = getAttributeData(comment,"id")
				comment_dict["comment_author"] = getAttributeData(comment,"author")
				comment_dict["comment_created_at"] = getAttributeData(comment,"created")
				comment_dict["comment_content"] = comment.childNodes[0].data
				comment_dict.update(issuedict)
				comment_list.append(comment_dict)
				# print("comment_name:%s"% comment.childNodes[0].data)
			# print(issuedict)
			# print(comment_list)
			commentsdf = pd.DataFrame(comment_list)
			result = pd.concat([result,commentsdf])
			# print(commentsdf)
			# print(result)
	return result

result_data = gread_all_xml(file_list)
result_data.to_csv('/Users/andiehuang/Lch/xml/xvm_data.csv')
# print(resule)

# def get_file_path(root_path,file_list,dir_list):
# 	dir_or_files = os.listdir(root_path)
# 	for dir_file in dir_or_files:
# 		dir_file_path = os.path.join(root_path,dir_file)
# 		if os.path.isdir(dir_file_path):
# 			dir_list.append(dir_file_path)
# 			get_file_path(dir_file_path,file_list,dir_list)
# 		else:
# 			file_list.append(dir_file_path)
# root_path = r"/Users/andiehuang/LCH/xml/"
# file_list = []
# dir_list = []
# get_file_path(root_path,file_list,dir_list)
# print(file_list)
# print (dir_list)
# for x in file_list:


