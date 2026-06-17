# MLTM_RXB_CALC_DUR_RULE_ORD_MAP

> Table used to store relationships between a drug, an order, and a dispense amount.

**Description:** MLTM_RXB_CALC_DUR_RULE_ORD_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOSE_DISPENSE_RULE_ID` | DOUBLE | NOT NULL | FK→ | FK to MLLD_RXB_CALC_DOSE_DISP_RULE |
| 2 | `DRUG_IDENTIFIER` | VARCHAR(15) | NOT NULL |  | Multum Drug ID |
| 3 | `DURATION_FACTOR` | VARCHAR(30) | NOT NULL |  | Duration factor to be used in RXB calculation rule. |
| 4 | `FREQUENCY_DURATION_RULE_ID` | DOUBLE | NOT NULL | FK→ | FK to MLLD_RXB_CALC_FREQ_DUR_RULE |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL |  | RxBuilder Order ID |
| 6 | `ROUNDING_MASK_ID` | DOUBLE | NOT NULL | FK→ | FK to MLLD_RXB_CALC_RND_MASK |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOSE_DISPENSE_RULE_ID` | [MLTM_RXB_CALC_DOSE_DISP_RULE](MLTM_RXB_CALC_DOSE_DISP_RULE.md) | `DOSE_DISPENSE_RULE_ID` |
| `FREQUENCY_DURATION_RULE_ID` | [MLTM_RXB_CALC_FREQ_DUR_RULE](MLTM_RXB_CALC_FREQ_DUR_RULE.md) | `FREQUENCY_DURATION_RULE_ID` |
| `ROUNDING_MASK_ID` | [MLTM_RXB_CALC_RND_MASK](MLTM_RXB_CALC_RND_MASK.md) | `ROUNDING_MASK_ID` |

