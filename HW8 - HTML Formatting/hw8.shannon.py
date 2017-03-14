#!/usr/bin/env python

###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################

#I worked with Ed Yip on this assignment

class Element(object):
	tag = "html"
	ind = "\t\t"

	def __init__(self, content = None, **kwargs):
		if content == None:
			self.content = []
		else:
			self.content = [content]
		self.attributes = ''.join(' {} = "{}"'.format(x, y) for x, y in kwargs.items())

	def append(self, new_content):
		self.content.append(new_content) 

	def render(self, file_out, ind=""):
		file_out.write("{}<{}{}>\n".format(ind, self.tag, self.attributes))
		for item in self.content:
			try:
				item.render(file_out, ind + self.ind) #recursive
			except:
				file_out.write("{}{}\n".format(ind + self.ind, item))
		file_out.write("{}</{}>\n".format(ind, self.tag))

class Html(Element):
	tag = "html"

	def render(self, file_out, ind=""):
		file_out.write("<!DOCTYPE html>\n")
		Element.render(self, file_out, ind)

class Body(Element):
	tag = "body"

class P(Element):
	tag = "p"

class Head(Element):
	tag = "head"

class Ul(Element):
    tag = 'u1'

class Li(Element):
    tag = 'li'

class OneLineTag(Element):
	tag = ""

	def render(self, file_out, ind=""):
		file_out.write("{}<{}{}>{}</{}>\n".format(ind, self.tag, self.attributes, self.content[0], self.tag))

class Title(OneLineTag):
	tag = "title"

class A(OneLineTag):
	tag = "a"

	def __init__(self, link, text):
		OneLineTag.__init__(self, text, href = link)

class H(OneLineTag):
    def __init__(self, counter, header):
        self.tag = 'h'+str(counter)
        Element.__init__(self, header)

class SelfClosingTag(Element):
    def render(self, file_out, ind=""):
        file_out.write('{}<{}{} />\n'.format(ind, self.tag, self.attributes))

class Hr(SelfClosingTag):
    tag = 'hr'

class Br(SelfClosingTag):
    tag = 'br'

class Meta(SelfClosingTag):
    tag = 'meta'
