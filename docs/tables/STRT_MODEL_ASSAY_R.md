# STRT_MODEL_ASSAY_R

> This is a many-to-many relationship resolution table between strt_model and strt_assay.

**Description:** This is a many-to-many relationship resolution table.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ASSAY_ALIAS` | VARCHAR(50) |  |  | Contains the assay alias returned by the model. |
| 2 | `DESCRIPTION` | CHAR(100) |  |  | A description of the assay's relationship to the model. |
| 3 | `FLUID_TYPE` | CHAR(2) |  |  | This column holds the fluid type for the associated assay. |
| 4 | `MODIFY_ALIAS_IND` | DOUBLE |  |  | Contains a Boolean integer indicating if the assay alias can be modified. |
| 5 | `PROCESS_SEQ` | DOUBLE |  |  | Reserved for future use. |
| 6 | `RESULT_TYPE_CD` | DOUBLE | NOT NULL |  | Contains the result type of the discrete assay for the model. |
| 7 | `STRT_ASSAY_ID` | DOUBLE | NOT NULL |  | Contains the DBMS assigned key field value from strt_assay table. |
| 8 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Contains the DBMS assigned key field value from strt_model table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

