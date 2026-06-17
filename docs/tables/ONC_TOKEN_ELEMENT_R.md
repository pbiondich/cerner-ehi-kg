# ONC_TOKEN_ELEMENT_R

> Relates doc set elements to defining characteristics of an oncology disease

**Description:** ONC_TOKEN_ELEMENT_R  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_SET_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the doc set element being related |
| 2 | `DOC_SET_REF_ID` | DOUBLE | NOT NULL | FK→ | Identifier for the doc set that contains the doc set element being related |
| 3 | `ONC_TOKEN_ELEMENT_R_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the Onc_token_element_r table. It is an internal system assigned number. |
| 4 | `STAGING_TOKEN_CD` | DOUBLE | NOT NULL |  | Identifies the staging token being related. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOC_SET_ELEMENT_ID` | [DOC_SET_ELEMENT_REF](DOC_SET_ELEMENT_REF.md) | `DOC_SET_ELEMENT_ID` |
| `DOC_SET_REF_ID` | [DOC_SET_REF](DOC_SET_REF.md) | `DOC_SET_REF_ID` |

