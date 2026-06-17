# MLTM_RXB_CALC_DOSE_DISP_RULE

> Table used to store relationships between France's UCD code and Multum Drug Identifier's for use with Millennium's order catalog

**Description:** MLTM_RXB_CALC_DOSE_DISP_RULE  
**Table type:** REFERENCE  
**Primary key:** `DOSE_DISPENSE_RULE_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISPENSE_UNIT_ID` | DOUBLE | NOT NULL |  | RxBuilder Dispense Unit ID |
| 2 | `DOSE_DISPENSE_RULE_ID` | DOUBLE | NOT NULL | PK | Externally generated sequence |
| 3 | `DOSE_UNIT_ID` | DOUBLE | NOT NULL |  | RxBuilder Dose Unit ID |
| 4 | `RATE_UNIT_ID` | DOUBLE | NOT NULL |  | RxBuilder Rate Unit ID |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MLTM_RXB_CALC_DISP_RULE_ORDMAP](MLTM_RXB_CALC_DISP_RULE_ORDMAP.md) | `DOSE_DISPENSE_RULE_ID` |
| [MLTM_RXB_CALC_DUR_RULE_ORD_MAP](MLTM_RXB_CALC_DUR_RULE_ORD_MAP.md) | `DOSE_DISPENSE_RULE_ID` |

