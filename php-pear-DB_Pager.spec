%include	/usr/lib/rpm/macros.php
%define         _class          DB
%define         _subclass       Pager
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Retrieve and return information of database result sets
Summary(pl):	%{_class}_%{_subclass} - Ściąganie i zwracanie informacji o zestawacanie rezultatów z baz danych
Name:		php-pear-%{_pearname}
Version:	0.7
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class handles all the stuff needed for displaying paginated
results from a database query of Pear DB. including fetching only the
needed rows and giving extensive information for helping build an HTML
or GTK query result display.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/%{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
