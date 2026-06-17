# MED_ADMIN_MED_EVENT_INGRDNT

> Meds Admin - Medication Event Ingredient Table

**Description:** Meds Admin - Medication Event Ingredient  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog code of the ingredient for the medication event. |
| 2 | `DRUG_FORM_CD` | DOUBLE | NOT NULL |  | The drug form of the ingredient for the medication event. |
| 3 | `IDENTIFICATION_PROCESS_CD` | DOUBLE | NOT NULL |  | The process used to identify the ingredient. |
| 4 | `MED_EVENT_INGREDIENT_ID` | DOUBLE | NOT NULL |  | The id of the medication event ingredient. |
| 5 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The foreign key to the parent table. |
| 6 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the parent table. |
| 7 | `STRENGTH` | DOUBLE | NOT NULL |  | The dose amount of the ingredient for the medication event (strength) |
| 8 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | The strength unit of the ingredient for the medication event. |
| 9 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The synonym id of the ingredient for the medication event. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `VOLUME` | DOUBLE | NOT NULL |  | The volume amount of the ingredient for the medication event. |
| 16 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | The volume unit of the ingredient for the medication event. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

