(function(){var e={},t=function(e){return document.getElementById(e)},n=function(e){return $("#"+e)},r="filter_list",i="filter_menu",s="input_filters",o="filter_detected",u="result_list";e.FILTERABLE={},e.NODE={},e.ALIAS={},e.TEMPLATES={},e.fullUpdate=function(){var t=y(),n=b(t),r=x(n),i=e.DATA,s=[],o=[],u=0;r.forEach(function(e){e!=null?(s=l(i,e,u),i=s,o.push({name:e.n,count:i.length,step:o.length}),u+=1):o.push({name:"???",unknown:!0,step:o.length})}),i.sort(a),u==0?(v(i),h([])):h(i),f(o)};var a=function(e,t){return t.m!=e.m?t.m-e.m:t.p-e.p},f=function(e){var t=Handlebars.templates.detectlist(e);n(o).html(t)},l=function(e,t,n){return fdata=[],e.forEach(function(e){var n=e.t;for(var r=0;r<n.length;r++)if(n[r]==t.i){fdata.push(e);return}}),fdata},c=function(t){var r=Handlebars.templates.filterlist(e.MODEL);n(i).html(r),t(null)},h=function(e,t){var r=Handlebars.templates.resultlist(e);n(u).html(r)},p=function(e){var t=Handlebars.templates.filterdetected(e);n(FILTER_DETECTED).html(t)},d=function(e,t,n){return fdata=[],e.forEach(function(e){var r=e.t;for(var i=t.length-1;i>=0;i--)for(var s=0;s<r.length;s++)if(r[s]==t[i]){n>0?e.match=e.match*((i+1)/t.length):e.match=(i+1)/t.length,fdata.push(e);return}}),fdata},v=function(e){e.forEach(function(e){e.match=1})},m=function(e){},g=function(){},y=function(){var e=n(s).val().trim().toLowerCase().split(" ");return e.filter(function(e){return e!=""})},b=function(e){return e},w=function(t){console.log("loading data.."),$.getJSON("data/data.json",function(n){e.DATA=n,console.log("loaded data!"),t(null)})},E=function(t){console.log("loading model.."),$.getJSON("data/model.json",function(n){e.MODEL=n,console.log("loaded model!"),t(null)})},S=function(t){T(e.MODEL),console.log("nodes",e.NODE),console.log("aliases",e.ALIAS),t(null)},x=function(t){var n=[];return t.forEach(function(t){var r=e.ALIAS[t];r?n.push(e.NODE[r]):n.push(null)}),n},T=function(t){e.ALIAS[t.i]=t.i;for(var n=0;n<t.a.length;n++)e.ALIAS[t.a[n]]=t.i;e.NODE[t.i]=t;if(t.s)for(var r=0;r<t.s.length;r++)T(t.s[r])},N=function(t,n){["filterlist","filterlistpartial"].forEach(function(t){e.TMPL[t]=Handlebars.templates[t+".tmpl"]})},C=function(t,n){n.push(t.i),e.ALIAS[t.i]=t.i;for(var r=0;r<t.a.length;r++)e.ALIAS[t.a[r]]=t.i;filterable={name:t.n,path:n},e.FILTERABLE[t.i]=filterable;if(t.s)for(var i=0;i<t.s.length;i++)buildFilterable(t.s[i],n.slice())},k=function(t){n(s).on("input",e.fullUpdate),$("div.add-filter").click(function(t){t.stopPropagation&&t.stopPropagation(),t&&t.currentTarget?(L($(t.currentTarget).attr("data-filter-id")),$(".ui.sidebar").sidebar("hide"),n(s).focus(),e.fullUpdate()):console.log(":S!!! No event.currentTarget")}),t(null)},L=function(e){var t=n(s),r=t.val().trim();r!=""&&t.val(t.val()+" "),t.val(t.val()+e)},A=function(e){$(".filter.menu .item").tab(),$(".ui.sidebar").sidebar("attach events","#button_addfilter"),$(".ui.accordion").first().accordion({selector:{title:".title.subs"}}),e(null)};e.init=function(){async.series([function(e){async.parallel([w,E],function(t,n){e(t)})},S,c,A,k])},this.inter=e})();