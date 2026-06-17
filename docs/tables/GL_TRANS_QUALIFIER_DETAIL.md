# GL_TRANS_QUALIFIER_DETAIL

> Stores qualifiers where there can be more than one possible data point.

**Description:** General Ledger Transaction Qualifier Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `GL_TRANS_QUALIFIER_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the gl_trans_qualifier_detail table. |
| 2 | `GL_TRANS_QUALIFIER_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related gl_trans_qualifier row. |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | This column represents the name of the qualifier being stored. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | This column contains the name of the qualifier being stored. |
| 5 | `QUALIFIER_TYPE_TXT` | VARCHAR(100) | NOT NULL |  | Describes what type of qualifier is being stored. |
| 6 | `QUALIFIER_VALUE` | VARCHAR(200) | NOT NULL |  | The qualifier value entered by the user for the corresponding qualifier type text. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `GL_TRANS_QUALIFIER_ID` | [GL_TRANS_QUALIFIER](GL_TRANS_QUALIFIER.md) | `GL_TRANS_QUALIFIER_ID` |

