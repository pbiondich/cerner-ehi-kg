# PRSNL_GROUP

> The personnel group table contains categories for identifying personnel with a common purpose, job,responsibility, specialty, credential, team, etc.

**Description:** Personnel Group  
**Table type:** REFERENCE  
**Primary key:** `PRSNL_GROUP_ID`  
**Columns:** 24  
**Referenced by:** 58 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 8 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 9 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 10 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 11 | `PRSNL_GROUP_CLASS_CD` | DOUBLE | NOT NULL |  | Personnel Group Classifications code identifies the classification of the group. (i.e. Physician gourp, Provider group, etc.) |
| 12 | `PRSNL_GROUP_DESC` | VARCHAR(255) |  |  | Text description of the prsnl group. Used to provider more detail. |
| 13 | `PRSNL_GROUP_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the personnel group table. It is an internal system assigned number. |
| 14 | `PRSNL_GROUP_NAME` | VARCHAR(100) |  |  | Name given to the personnel group. |
| 15 | `PRSNL_GROUP_NAME_KEY` | VARCHAR(100) |  |  | personnel group name key |
| 16 | `PRSNL_GROUP_NAME_KEY_A_NLS` | VARCHAR(400) |  |  | PRSNL_GROUP_NAME_KEY_A_NLS column |
| 17 | `PRSNL_GROUP_NAME_KEY_NLS` | VARCHAR(202) |  |  | This is the description used for non-English based strings for the NLSSORT function. |
| 18 | `PRSNL_GROUP_TYPE_CD` | DOUBLE | NOT NULL |  | Personnel Group Type Code identifies the type of group. (i.e. Surgeon, Vascular, Dental, etc.) |
| 19 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | Service Resource Code identifies the resource associated with the prsnl group. (i.e. Pharmacy, Surgery, etc.) |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (58)

| From table | Column |
|------------|--------|
| [AP_DC_EVENT](AP_DC_EVENT.md) | `PRSNL_GROUP_ID` |
| [AP_DC_EVENT_PRSNL](AP_DC_EVENT_PRSNL.md) | `PRSNL_GROUP_ID` |
| [AP_SYS_CORR](AP_SYS_CORR.md) | `ASSIGN_TO_GROUP_ID` |
| [CE_EVENT_ACTION](CE_EVENT_ACTION.md) | `ACTION_PRSNL_GROUP_ID` |
| [CE_EVENT_PRSNL](CE_EVENT_PRSNL.md) | `ACTION_PRSNL_GROUP_ID` |
| [CE_EVENT_PRSNL](CE_EVENT_PRSNL.md) | `REQUEST_PRSNL_GROUP_ID` |
| [CV_PROC](CV_PROC.md) | `PHYS_GROUP_ID` |
| [DA_DOCUMENT_PRSNL_RELTN](DA_DOCUMENT_PRSNL_RELTN.md) | `PRSNL_GROUP_ID` |
| [DCP_MP_PL_CUSTOM_ENTRY](DCP_MP_PL_CUSTOM_ENTRY.md) | `PRSNL_GROUP_ID` |
| [DCP_PL_CUSTOM_ENTRY](DCP_PL_CUSTOM_ENTRY.md) | `PRSNL_GROUP_ID` |
| [DCP_PL_QUERY_TEMP_ACCESS](DCP_PL_QUERY_TEMP_ACCESS.md) | `PROVIDER_GROUP_ID` |
| [DCP_PL_RELTN](DCP_PL_RELTN.md) | `PRSNL_GROUP_ID` |
| [ENCNTR_PRSNL_GRP_RELTN](ENCNTR_PRSNL_GRP_RELTN.md) | `PRSNL_GROUP_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `ORDERING_PHYS_GROUP_ID` |
| [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `RENDERING_PHYS_GROUP_ID` |
| [MESSAGING_FAVORITES](MESSAGING_FAVORITES.md) | `PRSNL_GROUP_ID` |
| [MESSAGING_NOTIFY](MESSAGING_NOTIFY.md) | `ASSIGN_PRSNL_GROUP_ID` |
| [MESSAGING_NOTIFY](MESSAGING_NOTIFY.md) | `NOTIFY_PRSNL_GROUP_ID` |
| [MESSAGING_OUT_OF_OFFICE](MESSAGING_OUT_OF_OFFICE.md) | `PRSNL_GROUP_ID` |
| [MP_PRIMED_VIEW_REF](MP_PRIMED_VIEW_REF.md) | `PRSNL_GROUP_ID` |
| [MSG_CONFIG_PUB_ASNMNT](MSG_CONFIG_PUB_ASNMNT.md) | `PRSNL_GROUP_ID` |
| [OMF_AUTH_PRSNL_GROUP](OMF_AUTH_PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |
| [OMF_PVI_FOLDERS](OMF_PVI_FOLDERS.md) | `PRSNL_GROUP_ID` |
| [OMF_PV_ITEMS](OMF_PV_ITEMS.md) | `PRSNL_GROUP_ID` |
| [ORDER_DAILY_REVIEW_DEFER](ORDER_DAILY_REVIEW_DEFER.md) | `DEFER_FROM_PRSNL_GROUP_ID` |
| [ORDER_DAILY_REVIEW_RSPNL](ORDER_DAILY_REVIEW_RSPNL.md) | `RSPNL_PRSNL_GROUP_ID` |
| [ORDER_NOTIFICATION](ORDER_NOTIFICATION.md) | `FROM_PRSNL_GROUP_ID` |
| [ORDER_NOTIFICATION](ORDER_NOTIFICATION.md) | `TO_PRSNL_GROUP_ID` |
| [ORDER_PROPOSAL_NOTIF](ORDER_PROPOSAL_NOTIF.md) | `FROM_PRSNL_GROUP_ID` |
| [ORDER_PROPOSAL_NOTIF](ORDER_PROPOSAL_NOTIF.md) | `TO_PRSNL_GROUP_ID` |
| [PATHWAY_NOTIFICATION](PATHWAY_NOTIFICATION.md) | `FORWARDING_PRSNL_GROUP_ID` |
| [PATHWAY_NOTIFICATION](PATHWAY_NOTIFICATION.md) | `FROM_PRSNL_GROUP_ID` |
| [PATHWAY_NOTIFICATION](PATHWAY_NOTIFICATION.md) | `TO_PRSNL_GROUP_ID` |
| [PFT_QUEUE_ASSIGNMENT](PFT_QUEUE_ASSIGNMENT.md) | `ASSIGNED_PRSNL_GROUP_ID` |
| [PFT_QUEUE_ITEM](PFT_QUEUE_ITEM.md) | `DEPARTMENT_ID` |
| [PFT_QUEUE_ITEM_WF_HIST](PFT_QUEUE_ITEM_WF_HIST.md) | `DEPARTMENT_ID` |
| [PFT_WF_DEPARTMENT_RELTN](PFT_WF_DEPARTMENT_RELTN.md) | `DEPARTMENT_ID` |
| [PRACTICE_SITE_MSG_ROUTING](PRACTICE_SITE_MSG_ROUTING.md) | `INTENDED_RECIP_PRSNL_GROUP_ID` |
| [PRACTICE_SITE_MSG_ROUTING](PRACTICE_SITE_MSG_ROUTING.md) | `ROUTED_RECIP_PRSNL_GROUP_ID` |
| [PREFERENCE_CARD](PREFERENCE_CARD.md) | `SURG_SPECIALTY_ID` |
| [PRSNL_GROUP_ORG_RELTN](PRSNL_GROUP_ORG_RELTN.md) | `PRSNL_GROUP_ID` |
| [PRSNL_GROUP_POOL](PRSNL_GROUP_POOL.md) | `PRSNL_GROUP_ID` |
| [PRSNL_GROUP_POOL_ROUTING_R](PRSNL_GROUP_POOL_ROUTING_R.md) | `PRSNL_GROUP_POOL_ID` |
| [PRSNL_ROLE_PROFILE](PRSNL_ROLE_PROFILE.md) | `CHART_ACCESS_PRSNL_GROUP_ID` |
| [RCM_CLARIFICATION](RCM_CLARIFICATION.md) | `PRSNL_GROUP_ID` |
| [RC_PRSNL_GROUP_EXCLUSION](RC_PRSNL_GROUP_EXCLUSION.md) | `PRSNL_GROUP_ID` |
| [RC_PRSNL_GROUP_INCLUSION](RC_PRSNL_GROUP_INCLUSION.md) | `PRSNL_GROUP_ID` |
| [RES_REVIEWER](RES_REVIEWER.md) | `PRSNL_GROUP_ID` |
| [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_SPECIALTY_ID` |
| [SURGICAL_PROCEDURE](SURGICAL_PROCEDURE.md) | `SURG_SPECIALTY_ID` |
| [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SCHED_SURG_SPECIALTY_ID` |
| [SURG_CASE_PROCEDURE](SURG_CASE_PROCEDURE.md) | `SURG_SPECIALTY_ID` |
| [SURG_PROC_DETAIL](SURG_PROC_DETAIL.md) | `SURG_SPECIALTY_ID` |
| [TASK_ACTIVITY](TASK_ACTIVITY.md) | `MSG_SENDER_PRSNL_GROUP_ID` |
| [TASK_ACTIVITY_ASSIGNMENT](TASK_ACTIVITY_ASSIGNMENT.md) | `ASSIGN_PRSNL_GROUP_ID` |
| [TASK_ACTIVITY_ASSIGN_MSG_H](TASK_ACTIVITY_ASSIGN_MSG_H.md) | `ASSIGN_PRSNL_GROUP_ID` |
| [TASK_ACTIVITY_MSG_H](TASK_ACTIVITY_MSG_H.md) | `MSG_SENDER_PRSNL_GROUP_ID` |
| [TEST_REVIEWER](TEST_REVIEWER.md) | `QUEUED_TO_PRSNL_GROUP_ID` |

