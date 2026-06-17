# MLLD_RXB_CALC_FREQ_DUR_RULE

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_RXB_CALC_FREQ_DUR_RULE  
**Table type:** REFERENCE  
**Primary key:** `FREQUENCY_DURATION_RULE_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DURATION_UNIT_ID` | DOUBLE | NOT NULL |  | RxBuilder Duration Unit Identifier |
| 2 | `FREQUENCY_DURATION_FACTOR` | VARCHAR(30) | NOT NULL |  | Factor text to be used for the Frequency Duration Rule |
| 3 | `FREQUENCY_DURATION_RULE_ID` | DOUBLE | NOT NULL | PK | Externally generated sequence |
| 4 | `FREQUENCY_ID` | DOUBLE | NOT NULL |  | RxBuilder Frequency Identifier |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MLLD_RXB_CALC_DISP_RULE_ORDMAP](MLLD_RXB_CALC_DISP_RULE_ORDMAP.md) | `FREQUENCY_DURATION_RULE_ID` |
| [MLLD_RXB_CALC_DUR_RULE_ORD_MAP](MLLD_RXB_CALC_DUR_RULE_ORD_MAP.md) | `FREQUENCY_DURATION_RULE_ID` |

