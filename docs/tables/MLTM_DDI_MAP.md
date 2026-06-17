# MLTM_DDI_MAP

> This table contains the mapping of an interaction text block to the drug-condition-plausibility combination via the dc_id field.

**Description:** Multum DDI Mapping  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 7

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DC_ID` | DOUBLE | NOT NULL | FK→ | The dc_id is assigned to a specific drug-condition-plausibility combination. FK from the MLTM_DDI_DRUG_CONDITION table. |
| 2 | `DDI_ID` | DOUBLE | NOT NULL | FK→ | drug-disease interaction text block identifier. FK from the MLTM_DDI_DESCRIPTION table. |
| 3 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 4 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 5 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 6 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 7 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DC_ID` | [MLTM_DDI_DRUG_CONDITION](MLTM_DDI_DRUG_CONDITION.md) | `DC_ID` |
| `DDI_ID` | [MLTM_DDI_DESCRIPTION](MLTM_DDI_DESCRIPTION.md) | `DDI_ID` |

