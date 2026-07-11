%global tl_name gzt
%global tl_revision 74605

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.5
Release:	%{tl_revision}.1
Summary:	Bundle of classes for La Gazette des Mathematiciens
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gzt
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gzt.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gzt.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gzt.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides two classes and BibLaTeX styles for the French
journal "La Gazette des Mathematiciens": gzt for the complete issues of
the journal, aimed at the Gazette's team, gztarticle, intended for
authors who wish to publish an article in the Gazette. This class's
goals are to faithfully reproduce the layout of the Gazette, thus
enabling the authors to be able to work their document in actual
conditions, and provide a number of tools (commands and environments) to
facilitate the drafting of documents, in particular those containing
mathematical formulas.

