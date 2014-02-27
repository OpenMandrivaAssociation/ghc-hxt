%global debug_package %{nil}
%define _cabal_setup Setup.lhs
%define module hxt

Summary:	A collection of tools for processing XML with Haskell
Name:		ghc-%{module}
Version:	9.3.1.1
Release:	2
License:	MIT
Group:		Development/Other
Url:		http://hackage.haskell.org/package/%{module}
Source0:	http://hackage.haskell.org/packages/archive/%{module}/%{version}/%{module}-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
BuildRequires:	ghc-devel
BuildRequires:	haddock
BuildRequires:	haskell-macros
BuildRequires:	haskell(HUnit)
BuildRequires:	haskell(hxt-charproperties)
BuildRequires:	haskell(hxt-regex-xmlschema)
BuildRequires:	haskell(hxt-unicode)
BuildRequires:	haskell(mtl)
BuildRequires:	haskell(network)
BuildRequires:	haskell(parsec)
Requires(post,preun):	ghc
Requires(pre):	haskell(HUnit)
Requires(pre):	haskell(hxt-charproperties)
Requires(pre):	haskell(hxt-regex-xmlschema)
Requires(pre):	haskell(hxt-unicode)
Requires(pre):	haskell(mtl)
Requires(pre):	haskell(network)
Requires(pre):	haskell(parsec)
Obsoletes:	haskell-%{module} < 9.3.1.1-2

%description
The Haskell XML Toolbox bases on the ideas of HaXml and HXML, but introduces a
more general approach for processing XML with Haskell.
The Haskell XML Toolbox uses a generic data model for representing XML
documents, including the DTD subset and the document subset, in Haskell.
It contains a validating XML parser, a HTML parser, namespace support, an XPath
expression evaluator, an XSLT library, a RelaxNG schema validator and funtions
for serialization and deserialization of user defined data.
The library makes extensive use of the arrow approach for processing XML.
Since version 9 the toolbox is partitioned into various (sub-)packages.
This package contains the core functionality, hxt-curl, hxt-tagsoup,
hxt-relaxng, hxt-xpath, hxt-xslt, hxt-regex-xmlschema contain the extensions.
hxt-unicode contains encoding and decoding functions,
hxt-charproperties char properties for unicode and XML.

%files
%{_docdir}/%{module}-%{version}
%{_libdir}/%{module}-%{version}
%{_cabal_rpm_deps_dir}
%{_cabal_haddoc_files}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{module}-%{version}

%build
%_cabal_build

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets

%check
%_cabal_check

