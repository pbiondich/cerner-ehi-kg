# CV_RESPONSE

> Reference table

**Description:** Reference table that stores information about responses for fields in a dataset.  
**Table type:** REFERENCE  
**Primary key:** `RESPONSE_ID`  
**Columns:** 26  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `A1` | VARCHAR(100) |  |  | Dependent on field_type(a,s,d,n) a : source value or d : date format (months=M, days=D, years=Y, hours=H, minutes=m, seconds=S, hundreths=h) n : #digits s : then #digits |
| 2 | `A2` | VARCHAR(50) |  |  | Dependent on field_type(a,s,d,n) a: destination value d: convert blank value to n: blank value to s : convert blank value to |
| 3 | `A3` | VARCHAR(50) |  |  | Dependent on field_type(a,s,d,n) a: d: convert unknown value to n: convert unknown value to s: convert to upper flag |
| 4 | `A4` | VARCHAR(50) |  |  | Dependent on field_type(a,s,d,n) a: d: n: minimum value s: |
| 5 | `A5` | VARCHAR(50) |  |  | Dependent on field_type(a,s,d,n) a: d: n: maximum value s: |
| 6 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 7 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 8 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 9 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 10 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 11 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 12 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 13 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 14 | `FIELD_TYPE` | VARCHAR(1) |  |  | Type of Field |
| 15 | `FIELD_TYPE_CD` | DOUBLE | NOT NULL |  | Type of Field Code. For future use. |
| 16 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL |  | Foreign Key. This is the primary indicator for the nomenclature table |
| 17 | `RESPONSE_ID` | DOUBLE | NOT NULL | PK | Primary key for this table. |
| 18 | `RESPONSE_INTERNAL_NAME` | VARCHAR(255) |  |  | The internal name used to store the Response Internal name. |
| 19 | `UPDT_APP` | DOUBLE |  |  | The front end application used to change records. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_REQ` | DOUBLE |  |  | The request number used to update records. |
| 25 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `XREF_ID` | DOUBLE | NOT NULL |  | Foreign Key for this table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CV_XREF_VALIDATION](CV_XREF_VALIDATION.md) | `RESPONSE_ID` |

