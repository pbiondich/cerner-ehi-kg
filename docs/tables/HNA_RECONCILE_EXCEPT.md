# HNA_RECONCILE_EXCEPT

> Stores the values that are excluded from reconcile.

**Description:** hna_reconcile_except  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 7 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 8 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `EXCEPTION_TYPE_CD` | DOUBLE | NOT NULL |  | Type of Exception (ex. lname, fname, alias, dob) |
| 11 | `EXCEPT_DT_TM` | DATETIME |  |  | Date and Time Field that hold a date if the exception type is date of birth (DOB) |
| 12 | `EXCEPT_GROUP_ID` | DOUBLE | NOT NULL |  | This id groups exceptions together so that multiple rows will act like one exception. (ex. fname = John lname = Doe SSN = 999999999" ) It is an internal system assigned number. |
| 13 | `EXCEPT_TEXT` | VARCHAR(100) |  |  | The Field where the text is stored for each exception. (ex. If the exception was lname = doe then the except_text field would equal "DOE".) |
| 14 | `GROUP_NAME` | VARCHAR(100) |  |  | Name give by the creator of the exception |
| 15 | `HNA_RECONCILE_EXCEPT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the hna_reconcile_except table. It is an internal system assigned number. |
| 16 | `POST_FLAG` | DOUBLE |  |  | Future ESI functionality. |
| 17 | `RECONCILE_FLAG` | DOUBLE |  |  | Determines if the exception is going to exclude person matching the exception from person reconcile. |
| 18 | `TEST_FLAG` | DOUBLE |  |  | Distinguishes between a test exception and a non-test exception. A test exception will be updated when you change the exception. A non-test exception will inactivate the old exception and create a new exception. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

