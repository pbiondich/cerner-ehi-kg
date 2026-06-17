# WP_TEMPLATE

> This reference table contains parameters associated with word processing templates. The template name, description, active/inactive indicator, template type (template versus letter, for example), activity type, and person ID are included.

**Description:** Word Processing Template  
**Table type:** REFERENCE  
**Primary key:** `TEMPLATE_ID`  
**Columns:** 13  
**Referenced by:** 23 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the activity type value for which the template was created. Activity types are stored on codeset 106. |
| 3 | `DESCRIPTION` | VARCHAR(60) |  |  | This field contains the description of the word processing template. |
| 4 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 5 | `RESULT_LAYOUT_EXISTS_IND` | DOUBLE | NOT NULL |  | Indicates whether the result layout exists. |
| 6 | `SHORT_DESC` | VARCHAR(25) |  |  | This field contains the short description (mnemonic) of the word processing template. |
| 7 | `TEMPLATE_ID` | DOUBLE | NOT NULL | PK | This field uniquely defines a row (a word processing template) included on the WP_TEMPLATE table. This field would be used to join to other tables (as a foreign key) such as the WP_TEMPLATE_TEXT reference table. |
| 8 | `TEMPLATE_TYPE_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the template type. Template types include options such as templates and letters, for example. Template type parameters are stored on codeset 1303. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (23)

| From table | Column |
|------------|--------|
| [AP_FT_TYPE](AP_FT_TYPE.md) | `DOCTOR_FINAL_TEMPLATE_ID` |
| [AP_FT_TYPE](AP_FT_TYPE.md) | `DOCTOR_FIRST_TEMPLATE_ID` |
| [AP_FT_TYPE](AP_FT_TYPE.md) | `DOCTOR_NOTIF_TEMPLATE_ID` |
| [AP_FT_TYPE](AP_FT_TYPE.md) | `PATIENT_FINAL_TEMPLATE_ID` |
| [AP_FT_TYPE](AP_FT_TYPE.md) | `PATIENT_FIRST_TEMPLATE_ID` |
| [AP_FT_TYPE](AP_FT_TYPE.md) | `PATIENT_NOTIF_TEMPLATE_ID` |
| [AP_PREFIX](AP_PREFIX.md) | `WORKSHEET_TEMPLATE_ID` |
| [ASSAY_PROCESSING_R](ASSAY_PROCESSING_R.md) | `DEFAULT_RESULT_TEMPLATE_ID` |
| [CSM_CAT_SUB_XREF](CSM_CAT_SUB_XREF.md) | `REQ_TEMPL_ID` |
| [CSM_CAT_SUB_XREF](CSM_CAT_SUB_XREF.md) | `RESL_TEMPL_ID` |
| [HIM_REQUEST_TEMPLATE_R](HIM_REQUEST_TEMPLATE_R.md) | `TEMPLATE_ID` |
| [MAMMO_FOL_UP_LETTER_SECT](MAMMO_FOL_UP_LETTER_SECT.md) | `TEMPLATE_ID` |
| [MAMMO_LETTER_DETAIL](MAMMO_LETTER_DETAIL.md) | `TEMPLATE_ID` |
| [MAMMO_NOTIFICATION](MAMMO_NOTIFICATION.md) | `TEMPLATE_ID` |
| [MAMMO_NOTIFICATION_HIST](MAMMO_NOTIFICATION_HIST.md) | `TEMPLATE_ID` |
| [RAD_FOLLOW_UP_DEFAULT](RAD_FOLLOW_UP_DEFAULT.md) | `TEMPLATE_ID` |
| [RAD_REPORT_DETAIL](RAD_REPORT_DETAIL.md) | `TEMPLATE_ID` |
| [RAD_TEMPLATE_ASSOC](RAD_TEMPLATE_ASSOC.md) | `TEMPLATE_ID` |
| [STATION](STATION.md) | `EOT_TEMPLATE_ID` |
| [STATION](STATION.md) | `TEMPLATE_ID` |
| [UCMR_KARYOTYPE_WP_TMPLT_R](UCMR_KARYOTYPE_WP_TMPLT_R.md) | `WP_TEMPLATE_ID` |
| [UCMR_LAYOUT_FIELD_TMPLT_R](UCMR_LAYOUT_FIELD_TMPLT_R.md) | `TEMPLATE_ID` |
| [WP_TEMPLATE_TEXT](WP_TEMPLATE_TEXT.md) | `TEMPLATE_ID` |

