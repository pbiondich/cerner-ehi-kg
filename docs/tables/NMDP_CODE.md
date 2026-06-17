# NMDP_CODE

> Contains the NMDP Codes that are generated from the NMDP Codes and HLA Alleles that have been entered.

**Description:** NMDP Code  
**Table type:** ACTIVITY  
**Primary key:** `NMDP_CODE_ID`  
**Columns:** 8  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `NMDP_CODE_DESC` | VARCHAR(255) |  |  | The description of the generated NMDP Code. |
| 2 | `NMDP_CODE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the nmdp_code table. It is an internal system assigned number. |
| 3 | `NMDP_SUFFIX_ID` | DOUBLE | NOT NULL | FK→ | Relates this NMDP Code to a NMDP Suffix. It is a foreign key reference to the primary key of the NMDP Suffix table. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NMDP_SUFFIX_ID` | [NMDP_SUFFIX](NMDP_SUFFIX.md) | `NMDP_SUFFIX_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [NMDP_ALLELE_XREF](NMDP_ALLELE_XREF.md) | `NMDP_CODE_ID` |

