# AP_FT_TYPE

> This reference table contains the basic parameters regarding follow-up tracking for cytology. Cases are optionally associated with a follow-up tracking type based on the alpha response value assigned to the diagnosis.

**Description:** AP Followup Tracking Type  
**Table type:** REFERENCE  
**Primary key:** `FOLLOWUP_TRACKING_TYPE_CD`  
**Columns:** 21  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DESCRIPTION` | VARCHAR(60) |  |  | This field contains the description of the follow-up tracking type. |
| 3 | `DOCTOR_FINAL_OVERDUE_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the patient's physician (the physician that submitted the cytology case that caused the follow-up event to be initiated) should receive a copy of the follow-up tracking final overdue report. |
| 4 | `DOCTOR_FINAL_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the follow-up report template used for the physician final overdue notification report. Template information is stored on the WP_TEMPLATE and WP_TEMPLATE_TEXT reference tables. |
| 5 | `DOCTOR_FIRST_OVERDUE_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the patient's physician (the physician that submitted the cytology case that caused the follow-up event to be initiated) should receive a copy of the follow-up tracking initial overdue report. |
| 6 | `DOCTOR_FIRST_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the follow-up report template used for the physician initial overdue notification report. Template information is stored on the WP_TEMPLATE and WP_TEMPLATE_TEXT reference tables. |
| 7 | `DOCTOR_NOTIFICATION_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the patient's physician (the physician that submitted the cytology case that caused the follow-up event to be initiated) should receive a copy of the follow-up initial notification report. |
| 8 | `DOCTOR_NOTIF_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the follow-up report template used for the physician initial notification report. Template information is stored on the WP_TEMPLATE and WP_TEMPLATE_TEXT reference tables. |
| 9 | `FOLLOWUP_TRACKING_TYPE_CD` | DOUBLE | NOT NULL | PK FK→ | This uniquely identifies a row included on the AP_FT_TYPE table. This field would be used to join to other tables (as a foreign key). The follow-up tracking type is also represented as an entry on codeset 1317. |
| 10 | `PATIENT_FINAL_OVERDUE_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the patient should receive a copy of the follow-up final overdue report. Note: This functionality is not yet available. |
| 11 | `PATIENT_FINAL_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the follow-up report template used for the patient final overdue report. Template information is stored on the WP_TEMPLATE and WP_TEMPLATE_TEXT reference tables. |
| 12 | `PATIENT_FIRST_OVERDUE_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the patient should receive a copy of the follow-up initial overdue report. Note: This functionality is not yet available. |
| 13 | `PATIENT_FIRST_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the follow-up report template used for the patient initial overdue report. Template information is stored on the WP_TEMPLATE and WP_TEMPLATE_TEXT reference tables. |
| 14 | `PATIENT_NOTIFICATION_IND` | DOUBLE |  |  | This field contains a flag value indicating whether or not the patient should receive a copy of the follow-up initial notification report. Note: This functionality is not yet available. |
| 15 | `PATIENT_NOTIF_TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the follow-up report template used for the patient initial notification report. Template information is stored on the WP_TEMPLATE and WP_TEMPLATE_TEXT reference tables. |
| 16 | `SHORT_DESC` | VARCHAR(25) |  |  | This field contains the short description (mnemonic) of the follow-up tracking type. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOCTOR_FINAL_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `DOCTOR_FIRST_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `DOCTOR_NOTIF_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `FOLLOWUP_TRACKING_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PATIENT_FINAL_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `PATIENT_FIRST_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |
| `PATIENT_NOTIF_TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [AP_FT_EVENT](AP_FT_EVENT.md) | `FOLLOWUP_TYPE_CD` |
| [AP_FT_REPORT_PROC](AP_FT_REPORT_PROC.md) | `FOLLOWUP_TRACKING_TYPE_CD` |
| [AP_FT_TERM_PROC](AP_FT_TERM_PROC.md) | `FOLLOWUP_TRACKING_TYPE_CD` |
| [CYTO_ALPHA_SECURITY](CYTO_ALPHA_SECURITY.md) | `FOLLOWUP_TRACKING_TYPE_CD` |

