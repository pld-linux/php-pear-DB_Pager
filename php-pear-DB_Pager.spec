%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	Pager
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - retrieve and return information of database result sets
Summary(pl):	%{_pearname} - pobieranie i zwracanie informacji o zestawacanie rezultatów z baz danych
Name:		php-pear-%{_pearname}
Version:	0.7
Release:	3
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	ec4213fe39bdfab951b14433a6ae60c0
URL:		http://pear.php.net/package/DB_Pager/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class handles all the stuff needed for displaying paginated
results from a database query of PEAR DB, including fetching only the
needed rows and giving extensive information for helping build an HTML
or GTK query result display.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa obs³uguje wszystko co potrzebne do wy¶wietlania
stronicowanych wyników z zapytania do bazy PEAR DB, w³±cznie ze
¶ci±ganiem tylko potrzebnych wierszy i dawaniem szczegó³owych
informacji pomocnych przy wy¶wietlaniu wyników zapytania w HTML-u lub
GTK.

Ta klasa ma w PEAR status: %{_status}.

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
