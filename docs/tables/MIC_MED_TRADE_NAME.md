# MIC_MED_TRADE_NAME

> This table contains the generic trade name, route and dosage information defined for each antibiotic.

**Description:** Microbiology Medication Trade Name  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHART_IND` | DOUBLE |  |  | This field indicates whether the trade name should be included in inquiry applications and on patient reports. Valid values include: 0 = Do not chart 1 = Chart |
| 2 | `COST_PER_DOSE` | VARCHAR(10) |  |  | This field identifies the cost per dose of the antibiotic for the defined trade name. |
| 3 | `DOSAGE` | VARCHAR(30) |  |  | This field identifies the standard dosage of the antibiotic for the defined trade name. |
| 4 | `PRIMARY_IND` | DOUBLE |  |  | This field indicates whether the trade name is the primary trade name. Charting will able to be defined such that either all trade names print on patient reports or only the primary trade name. Valid values include: 0 = Not the primary trade name 1 = Primary trade name |
| 5 | `TASK_COMPONENT_CD` | DOUBLE | NOT NULL | FK→ | This field identifies the code_value of the antibiotic to which the trade name is associated. Antibiotics are defined on code set 1011 Antibiotics(Medications) |
| 6 | `TRADE_NAME` | VARCHAR(50) |  |  | This field identifies the generic trade name associated with the antibiotic. |
| 7 | `TRADE_NAME_SEQ` | DOUBLE | NOT NULL |  | This field contains a unique value for each trade name associated with an antibiotic. The first trade name would be assigned sequence 1, and the second trade name would be assigned sequence 2, etc. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TASK_COMPONENT_CD` | [MIC_DETAIL_TASK](MIC_DETAIL_TASK.md) | `TASK_COMPONENT_CD` |

