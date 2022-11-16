Name:		texlive-gzt
Version:	63591
Release:	1
Summary:	Bundle of classes for "La Gazette des Mathematiciens"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gzt
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gzt.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gzt.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gzt.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides two classes and BibLaTeX styles for the
French journal "La Gazette des Mathematiciens": gzt for the
complete issues of the journal, aimed at the Gazette's team,
gztarticle, intended for authors who wish to publish an article
in the Gazette. This class's goals are to faithfully reproduce
the layout of the Gazette, thus enabling the authors to be able
to work their document in actual conditions, and provide a
number of tools (commands and environments) to facilitate the
drafting of documents, in particular those containing
mathematical formulas.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/gzt
%{_texmfdistdir}/tex/latex/gzt
%doc %{_texmfdistdir}/doc/latex/gzt

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
