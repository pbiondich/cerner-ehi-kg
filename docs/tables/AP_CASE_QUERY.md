# AP_CASE_QUERY

> This reference table includes basic parameters regarding an established case query. Detail parameters associated with the query are stored on the AP_CASE_QUERY_DETAILS table.

**Description:** AP Case Query  
**Table type:** ACTIVITY  
**Primary key:** `CASE_QUERY_ID`  
**Columns:** 17  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | This is the Activity Type Cd of the product owning the Query. If this value is 0 it will be assumed to be AP. |
| 2 | `CASE_QUERY_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code which uniquely identifies the case retrieval query (and its associated parameters). This value is used to join to other tables, such as the AP_CASE_QUERY_DETAILS table. |
| 3 | `NBR_COPIES` | DOUBLE |  |  | This field contains the "number of copies" value specified by the user when the case query was executed. |
| 4 | `OUTPUT_DEST_ID` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the output destination (related to a printer and a print queue) used to print the results of the case query. |
| 5 | `QUERY_START_DT_TM` | DATETIME |  |  | This field contains the date and time the user submitted the query. |
| 6 | `REPORT_HISTORY_CD` | DOUBLE | NOT NULL |  | This field contains the internal identification code of the report history grouping associated with the report query. The history grouping specifies the report component sections (discrete tasks) that will print on the report (if report text is printed). |
| 7 | `REPORT_TYPE_FLAG` | DOUBLE |  |  | This flag value specifies how the pathology reports qualifying for this query should be viewed. A value of "1" indicates that a summary (report parameters) view is used, while a value of "2" indicates that a detail (result text and codes) view is used. |
| 8 | `RESULT_NAME` | VARCHAR(100) |  |  | This field contains the 'Query Result Name' for this case query. This field is only filled out when the person initiating the query is saving query results. |
| 9 | `RESULT_NAME_KEY` | VARCHAR(100) |  |  | This field contains the same value as the result_name column converted to uppercase. |
| 10 | `SEARCH_TYPE_FLAG` | DOUBLE |  |  | This flag value documents how the reports should be searched for cases qualifying for this query. A value of "1" indicates that the search is at the report level, while a value of "2" indicates that the search is at the report component (discrete task) level. |
| 11 | `STARTED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code associated with the user who submitted the report query. |
| 12 | `STATUS_FLAG` | DOUBLE |  |  | This field includes a flag value denoting the current status of the query. A value of "1" indicates that the query is pending. A status of "2" indicates that the query is in process. A status of "3" indicates that the query was cancelled. A status of "4" indicates that the query was completed. A status of "5" indicates that the execution of the query encountered an error. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STARTED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [AP_CASE_QUERY_DETAILS](AP_CASE_QUERY_DETAILS.md) | `CASE_QUERY_ID` |
| [AP_QUERY_RESULT](AP_QUERY_RESULT.md) | `CASE_QUERY_ID` |

