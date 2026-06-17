# CASE_REPORT

> This activity table contains entries for all current cases having one or more reports associated. The case/report relationship is stored. The ID of the user who ordered the report is stored, as is the current report status and cancellation information.

**Description:** Case Report  
**Table type:** ACTIVITY  
**Primary key:** `REPORT_ID`  
**Columns:** 21  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BLOB_BITMAP` | DOUBLE |  |  | This field contains a value that indicates whether there is any special blob data that is associated to this report (i.e. images). |
| 2 | `CANCEL_CD` | DOUBLE | NOT NULL |  | If a report has been updated to a cancelled status, this field includes the identification code assigned to the cancellation reason specified by the user performing the cancellation activity. |
| 3 | `CANCEL_DT_TM` | DATETIME |  |  | If a report has been updated to a cancelled status, this field contains the date and time the cancellation activity occurred. |
| 4 | `CANCEL_PRSNL_ID` | DOUBLE | NOT NULL |  | If a report has been updated to a cancelled status, this field contains the internal identification code associated with the user who cancelled the report. This ID could be used to access user information by joining to the PRSNL or PERSON tables. |
| 5 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 6 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the unique internal reference of the report order catalog item associated with the case. This ID could be used to access order catalog information for the report by joining to the order catalog tables. |
| 7 | `EVENT_ID` | DOUBLE | NOT NULL |  | This field contains the unique internal reference of the report to the report information stored in the Clinical_Event table. |
| 8 | `REPORT_ID` | DOUBLE | NOT NULL | PK | This field uniquely defines a row included on the CASE_REPORT table (the specific case and report reference). This field would be used to join to other tables (as a foreign key) such as the REPORT_TASK table. |
| 9 | `REPORT_SEQUENCE` | DOUBLE | NOT NULL |  | This field contains a numeric value that is used to sequence reports when a single report order catalog item has been ordered more than one time for a single case. For example, this field would be used to sequence addendum #1 and addendum #2. |
| 10 | `REQUEST_DT_TM` | DATETIME |  |  | This field contains the date and time the report was ordered. |
| 11 | `REQUEST_PRSNL_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the user who ordered the report. This value could be used to join to personnel information included on the PRSNL or PERSON tables. |
| 12 | `SIGNING_LOCATION_CD` | DOUBLE | NOT NULL |  | Lab facility or location where case was read and diagnosed. |
| 13 | `STATUS_CD` | DOUBLE | NOT NULL |  | This field contains the report status code ID value. Report status codes are stored on codeset 1305. |
| 14 | `STATUS_DT_TM` | DATETIME |  |  | This field contains the date and time the report reached the status identified in the STATUS_CD field. |
| 15 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code associated with the user who caused the report to be updated to the status stored in the STATUS_CD field. This value could be used to join to personnel information on the PRSNL and PERSON tables. |
| 16 | `SYNOPTIC_STALE_DT_TM` | DATETIME |  |  | This field indicates if the synoptic generated text in a report section on this report has become stale or is in need of regenerating text based on changes in specimen or Synoptic worksheet data. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [AP_CASE_SYNOPTIC_WS](AP_CASE_SYNOPTIC_WS.md) | `REPORT_ID` |
| [AP_TRANS_STAT](AP_TRANS_STAT.md) | `REPORT_ID` |
| [REPORT_DETAIL_IMAGE](REPORT_DETAIL_IMAGE.md) | `REPORT_ID` |
| [REPORT_QUEUE_R](REPORT_QUEUE_R.md) | `REPORT_ID` |
| [REPORT_TASK](REPORT_TASK.md) | `REPORT_ID` |

