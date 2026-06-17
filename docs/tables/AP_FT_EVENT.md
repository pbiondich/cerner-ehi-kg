# AP_FT_EVENT

> This activity table contains parameters associated with a follow-up tracking event. Follow-up activities are triggered by the verification of a cytology report. The event created is determined by the alpha response diagnosis value assigned to the report.

**Description:** AP Followup Tracking Event  
**Table type:** ACTIVITY  
**Primary key:** `FOLLOWUP_EVENT_ID`  
**Columns:** 25  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CASE_ID` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to case information stored on the PATHOLOGY_CASE activity table. |
| 2 | `EXPECTED_TERM_DT` | DATETIME |  |  | This field contains the expected termination date for the follow-up tracking event. This date is calculated based on the report diagnosis alpha response value, and indicates the date the event is scheduled to be deleted from the table. |
| 3 | `FINAL_OVERDUE_DT_TM` | DATETIME |  |  | This field contains the scheduled final overdue notification date for the follow-up event. This date is calculated based on the report diagnosis alpha value, and indicates the date the event is scheduled to print on the final overdue report. |
| 4 | `FINAL_OVERDUE_PRINT_FLAG` | DOUBLE |  |  | This field contains a numeric flag value indicating whether or not the follow-up tracking event has been included (printed) on a final overdue report. |
| 5 | `FIRST_OVERDUE_DT_TM` | DATETIME |  |  | This field contains the scheduled initial overdue notification date for the follow-up event. This date is calculated based on the report diagnosis alpha value, and indicates the date the event is scheduled to print on the initial overdue report. |
| 6 | `FIRST_OVERDUE_PRINT_FLAG` | DOUBLE |  |  | This field contains a numeric flag value indicating whether or not the follow-up tracking event has been included (printed) on an initial overdue report. |
| 7 | `FOLLOWUP_EVENT_ID` | DOUBLE | NOT NULL | PK | This field uniquely defines a row included on the AP_FT_EVENT table. This field would be used to join to other tables (as a foreign key) such as the FT_TERM_CANDIDATE_LIST activity table. |
| 8 | `FOLLOWUP_TYPE_CD` | DOUBLE | NOT NULL | FK→ | This field contains the foreign key value used to join to the follow-up tracking type codeset (codeset 1317). |
| 9 | `INITIAL_NOTIF_DT_TM` | DATETIME |  |  | This field contains the scheduled initial notification date for the follow-up event. This date is calculated based on the report diagnosis alpha response value, and indicates the date the event is scheduled to print on the follow-up notification report. |
| 10 | `INITIAL_NOTIF_PRINT_FLAG` | DOUBLE |  |  | This field contains a numeric flag value indicating whether or not the follow-up tracking event has been included (printed) on an initial notification report. |
| 11 | `ORIGIN_DT_TM` | DATETIME |  |  | This field contains the date and time the follow-up tracking event record was added to this table. |
| 12 | `ORIGIN_FLAG` | DOUBLE |  |  | This field contains a numeric flag value indicating how the follow-up tracking event record was added to this table. Fields can be added by the system (automatically based the verification of a cytology report) or manually (entered by a user). |
| 13 | `ORIGIN_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | If the event record was manually added to the table, this field contains the user's internal ID value. This value could be used to join to personnel information on the PRSNL or PERSON tables. If the record was system-added, the field includes a zero. |
| 14 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 15 | `TERM_ACCESSION_NBR` | CHAR(21) |  |  | This field contains the terminating case number entered by the user or system when the follow-up tracking event was updated to a terminated status. |
| 16 | `TERM_COMMENT` | VARCHAR(100) |  |  | This field is no longer used. Refer to the term_long_text_id for comment information. |
| 17 | `TERM_DT_TM` | DATETIME |  |  | If the follow-up tracking event was terminated, this field contains the date and time the follow-up tracking event was updated to a terminated status. |
| 18 | `TERM_ID` | DOUBLE | NOT NULL | FK→ | If the event record was manually terminated, this field contains the user's internal ID value. This value could be used to join to personnel information on the PRSNL or PERSON tables. If the record was system-terminated, the field includes a zero. |
| 19 | `TERM_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the value representing the entry on the LONG_TEXT table that contains the termination comment. |
| 20 | `TERM_REASON_CD` | DOUBLE | NOT NULL |  | If the follow-up tracking event was terminated, this field contains the termination reason code ID value. Termination reason codes are stored on codeset 1313. |
| 21 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 22 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 23 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 24 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_ID` | [PATHOLOGY_CASE](PATHOLOGY_CASE.md) | `CASE_ID` |
| `FOLLOWUP_TYPE_CD` | [AP_FT_TYPE](AP_FT_TYPE.md) | `FOLLOWUP_TRACKING_TYPE_CD` |
| `ORIGIN_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `TERM_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `TERM_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [FT_TERM_CANDIDATE_LIST](FT_TERM_CANDIDATE_LIST.md) | `FOLLOWUP_EVENT_ID` |

