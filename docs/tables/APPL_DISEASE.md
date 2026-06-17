# APPL_DISEASE

> The applicable disease for the amendment

**Description:** The applicable diseases for the amendment  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APPL_DISEASE_DESC_OTR` | VARCHAR(255) |  |  | Description of the disease |
| 2 | `APPL_DISEASE_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the appl_disease table. It is an internal system assigned number. |
| 3 | `DISEASE_SUB_TYPE_CD` | DOUBLE | NOT NULL |  | Disease sub-type |
| 4 | `DISEASE_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of disease |
| 5 | `PROT_AMENDMENT_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the prot_amendment table. It is an internal system assigned number. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PROT_AMENDMENT_ID` | [PROT_AMENDMENT](PROT_AMENDMENT.md) | `PROT_AMENDMENT_ID` |

