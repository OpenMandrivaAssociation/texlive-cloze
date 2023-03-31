Name:		texlive-cloze
Version:	55763
Release:	2
Summary:	A LuaLaTeX package for creating cloze texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cloze
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cloze.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cloze.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cloze.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LuaTeX or LuaLaTeX package for generating cloze
texts. The main feature of the package is that the formatting
doesn't change when using the hide and show options. There are
the commands \cloze, \clozefix, \clozefil, \clozenol,
\clozestrike and the environments clozepar and clozebox to
generate cloze texts.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/luatex/cloze
%{_texmfdistdir}/tex/luatex/cloze
%{_texmfdistdir}/scripts/cloze
%doc %{_texmfdistdir}/doc/luatex/cloze

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
