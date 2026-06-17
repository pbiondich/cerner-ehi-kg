# AP_QUERY_RESULT

> This activity table contains the pathology case number which have qualified for a given Case Retrieval query.

**Description:** AP Case Query Result  
**Table type:** ACTIVITY  
**Primary key:** `QUERY_RESULT_ID`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCESSION_NBR` | CHAR(21) |  |  | This field contains the case number which has qualified for a given Case Query. |
| 2 | `CASE_QUERY_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identification code which uniquely identifies the case retrieval query (and its associated parameters). This value is used to join to the AP_CASE_QUERY table. |
| 3 | `EVENT_ID` | DOUBLE | NOT NULL |  | This is the MDOC level event ID of the report that qualified |
| 4 | `QUERY_RESULT_ID` | DOUBLE | NOT NULL | PK | This field contains the internal identification code which uniquely identifies this row on the ap_query_result table. This value is used to join to the AP_QUERY_RESULT_OFFSET table. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CASE_QUERY_ID` | [AP_CASE_QUERY](AP_CASE_QUERY.md) | `CASE_QUERY_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [AP_QUERY_RESULT_OFFSET](AP_QUERY_RESULT_OFFSET.md) | `QUERY_RESULT_ID` |

