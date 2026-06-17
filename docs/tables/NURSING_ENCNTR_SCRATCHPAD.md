# NURSING_ENCNTR_SCRATCHPAD

> Maintains scratchpad data for a given time period of a solution

**Description:** NURSING_ENCNTR_SCRATCHPAD  
**Table type:** ACTIVITY  
**Primary key:** `NURSING_ENCNTR_SCRATCHPAD_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter id that relates to the scratchpad information being stored |
| 2 | `LAST_UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the scratchpad information was last updated |
| 3 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Identifier that relates NURSING_ENCNTR_SCRATCHPAD rows to LONG_BLOB table (this field will become logically obsolete after addition of field SCRATCHPAD_BLOB to the table) |
| 4 | `NURSING_ENCNTR_SCRATCHPAD_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The id of the person responsible for documenting the scratchpad information |
| 6 | `SCRATCHPAD_TYPE_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE ** - this column becomes OBSOLETE after new column SCRATCHPAD_TYPE_NAME, is added to the table.Categorizes the scratchpad into a logical group or type. Example is MEDADMINCHRT |
| 7 | `SCRATCHPAD_TYPE_NAME` | VARCHAR(50) |  |  | Indicates the type of scratchpad entry in the NURSING_ENCTR_SCRATCHPAD table |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [NC_CHARTED_VIEW](NC_CHARTED_VIEW.md) | `SCRATCHPAD_DRAFT_ID` |

