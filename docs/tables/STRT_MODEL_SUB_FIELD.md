# STRT_MODEL_SUB_FIELD

> This table will describe the sub fields that make up a composite assay.

**Description:** Starter Model Sub Field  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DELIMITER` | CHAR(1) |  |  | This is the character that will be used as the delimiter between sub-fields. The default is "\|", if this field is empty. |
| 2 | `DESCRIPTION` | VARCHAR(200) |  |  | Description of the assay sub field. |
| 3 | `DIRECTION_FLAG` | DOUBLE | NOT NULL |  | Flag used to determine the direction of an alias; 1-Upload, 2- Download, 3 - Both. |
| 4 | `DISPLAY` | VARCHAR(30) |  |  | The header information for the Sub Field |
| 5 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | The defined SUB_FIELD is related to this Starter Model. |
| 6 | `STRT_MODEL_SUB_FIELD_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 7 | `SUB_FIELD_SEQ` | DOUBLE |  |  | The sequence position of this record in regards to the associated strt_model_id |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

