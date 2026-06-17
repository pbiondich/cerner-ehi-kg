# MLLD_RXB_CALC_RND_MASK

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_RXB_CALC_RND_MASK  
**Table type:** REFERENCE  
**Primary key:** `ROUNDING_MASK_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DECIMAL_PRECISION` | DOUBLE | NOT NULL |  | Identifies decimal precision to be used |
| 2 | `ROUNDING_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Identifies the rounding format ID |
| 3 | `ROUNDING_MASK_ID` | DOUBLE | NOT NULL | PK | Primary key for table. Externally generated ID |
| 4 | `SIGNIFICANT_DIGIT` | DOUBLE | NOT NULL |  | Identifies the significant digit for rounding |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ROUNDING_FORMAT_ID` | [MLLD_RXB_CALC_RND_FORMAT](MLLD_RXB_CALC_RND_FORMAT.md) | `FORMAT_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [MLLD_RXB_CALC_DISP_RULE_ORDMAP](MLLD_RXB_CALC_DISP_RULE_ORDMAP.md) | `ROUNDING_MASK_ID` |
| [MLLD_RXB_CALC_DUR_RULE_ORD_MAP](MLLD_RXB_CALC_DUR_RULE_ORD_MAP.md) | `ROUNDING_MASK_ID` |

