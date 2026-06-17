# AP_QUERY_RESULT_OFFSET

> This activity table is NOT currently is use. In the future, this table will contain lenght/offset of freetext data which is used to qualify the a Case Query.

**Description:** AP Case Query Result Offset  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | This is the unique identifier of the CE_BLOB which qualified within the free textCase Query Retrieval. |
| 2 | `LENGTH` | DOUBLE |  |  | This field contains the text length from the CE_BLOB table which was used to qualify the event in the Case Query. |
| 3 | `OFFSET` | DOUBLE |  |  | This field contains the text offset within the CE_BLOB table which was used to qualify the event in the Case Query. |
| 4 | `QUERY_RESULT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the internal identificationcode which uniquely identifies the ap_query_result this row is associated with. This column along with the SEQUENCE column make of the primary key for this table. |
| 5 | `SEQUENCE` | DOUBLE | NOT NULL |  | This field contains a sequential value which is used with the QUERY_RESULT_ID in order to make this a unique row within this table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `QUERY_RESULT_ID` | [AP_QUERY_RESULT](AP_QUERY_RESULT.md) | `QUERY_RESULT_ID` |

