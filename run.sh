curl 'https://anc.ca.apm.activecommunities.com/activekitchener/rest/activities/list?locale=en-US' \
  \
  -H 'page_info: {"order_by":"Date range","page_number":1,"total_records_per_page":20}' \
  \
  -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36' \
  -H 'Content-Type: application/json;charset=utf-8' \
  --data-raw '{"activity_search_pattern":{"skills":[],"time_after_str":"","days_of_week":null,"activity_select_param":0,"center_ids":["4"],"time_before_str":"","open_spots":null,"activity_id":null,"activity_category_ids":[],"date_before":"","min_age":null,"date_after":"","activity_type_ids":[],"site_ids":[],"for_map":false,"geographic_area_ids":[],"season_ids":[],"activity_department_ids":[],"activity_other_category_ids":[],"child_season_ids":[],"activity_keyword":"","instructor_ids":[],"max_age":null,"custom_price_from":"","custom_price_to":""},"activity_transfer_pattern":{}}'

# -H 'Accept: */*' \
# -H 'Accept-Language: en,es-MX;q=0.9,es;q=0.8' \
# -H 'Connection: keep-alive' \
# -H $'Cookie: LOGIN_FAILURES=0; org=activekitchener; TS0178a0b2=01e462b1a2c6fc7bf44ad0936d8e4b36cef4679d3fa7ce0505c538fb14b1b62e13bd8563cf66bf998ea2f29ef02aeccd31a70784be7fa85e5157d00a7786afe28260402fc209a0803a40e194a92cda699e588632fe; TS01b919ad=01e462b1a25c3f91bc7977fb2494b4933d0a80b18ea7ce0505c538fb14b1b62e13bd8563cf71103308e55c285d039f4a4f162631dbcefb0177b9c8bbd2ba83398c487ce551; activekitchener_FullPageView=true; BIGipServer~activenet~anc_prodca_activekitchener=\u0021ZDmMoZtiRkmp5RKR7r6iH/McDR2flC285hZAfRm8gUz443c12+vCZRno+MCDBYDyrvf0rBBQI1rCZQ==; BIGipServer~activenet~activenet_cui_prod_ats=\u0021H7Tg6gtSO20tScaR7r6iH/McDR2flMqe0NnbAbRNzPZ7fAyFXchSOX9K8ZAz0Iz9uL773I4dgJG0S/o=; activekitchener_locale=en-US; s_fid=0D5CA07B2E551EDA-377789B8B5CB7E89; s_cc=true; activekitchener_LOGGED_JSESSIONID=node018t95o32bvit6386cidc8u9m3277766.node0; activekitchener_JSESSIONID=node018t95o32bvit6386cidc8u9m3277766.node0; activekitchener_NEW_CUI_STATUS=true; JSESSIONID=node03rb14597qn2l1beivballwuj6352343.node0; TS012d8099=01e462b1a2d2d3c4bfe1b30dd9ebe12fc06bf8f22e3693c15012c75976c977490935abf2ffc2937dc70686b57b3556ee2aabfe543ca44c626833577893404d72b1ca4725fd5b7ec138c5e96816c7b69f76e628f659; TS01e1328e=01e462b1a24e2fa6c5867e10a248ab8f6ae6e846043693c15012c75976c977490935abf2ff499d5aab4cd31195944a0a9d2d81850f20f667a916dcd18cd6b1b02bd73609543eae5f82f9f19bea14793ee1d88f2a158bbbcd7956b9a5853bb50f9aaa24da315e3aa3c4cc2b45dbed0f09cc98adf410; utag_main=_sn:1$_se:20%3Bexp-session$_ss:0%3Bexp-session$_st:1750991880774%3Bexp-session$ses_id:1750990032773%3Bexp-session$_pn:5%3Bexp-session$vapi_domain:activecommunities.com; s_sq=anactivenet%3D%2526c.%2526a.%2526activitymap.%2526page%253Danc.ca.apm.activecommunities.com%25252Factivekitchener%25252Factivity%25252Fsearch%2526link%253DApply%2526region%253Dmain-content-body%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253Danc.ca.apm.activecommunities.com%25252Factivekitchener%25252Factivity%25252Fsearch%2526pidt%253D1%2526oid%253Dfunctioncn%252528%252529%25257B%25257D%2526oidt%253D2%2526ot%253DSUBMIT' \
# -H 'DNT: 1' \
# -H 'Origin: https://anc.ca.apm.activecommunities.com' \
# -H 'Referer: https://anc.ca.apm.activecommunities.com/activekitchener/activity/search?onlineSiteId=0&locale=en-US&activity_select_param=0&center_ids=4&viewMode=list' \
# -H 'Sec-Fetch-Dest: empty' \
# -H 'Sec-Fetch-Mode: cors' \
# -H 'Sec-Fetch-Site: same-origin' \
# -H 'X-CSRF-Token: 2fe71fca-308e-417c-bb74-81a6b8b68901' \
# -H 'sec-ch-ua: "Chromium";v="117", "Not;A=Brand";v="8"' \
# -H 'sec-ch-ua-mobile: ?0' \
# -H 'sec-ch-ua-platform: "Linux"' \
# --compressed
