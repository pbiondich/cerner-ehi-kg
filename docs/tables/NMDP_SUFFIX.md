# NMDP_SUFFIX

> Defines the NMDP Code used as the suffix to an HLA allele to designate a group of alleles.

**Description:** NMDP Suffix  
**Table type:** REFERENCE  
**Primary key:** `NMDP_SUFFIX_ID`  
**Columns:** 11  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EXAMPLE_SUBTYPE` | VARCHAR(255) |  |  | An example set of Alleles that could make up the NMDP Code. |
| 2 | `GENERATED_IND` | DOUBLE |  |  | Indicates whether the NMDP Code as been generated. |
| 3 | `NMDP_SEQUENCE` | DOUBLE |  |  | Defines the order the NMDP Codes. |
| 4 | `NMDP_SUFFIX_DESC` | CHAR(10) |  |  | The description assigned to the NMDP Code. Unique identifier the user gives the NMDP Code. |
| 5 | `NMDP_SUFFIX_ID` | DOUBLE | NOT NULL | PK | A sequentially assigned number which uniquely identifies a NMDP Suffix record. |
| 6 | `REMOVED_IND` | DOUBLE |  |  | Indicates whether the NMDP Code as been removed. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [NMDP_CODE](NMDP_CODE.md) | `NMDP_SUFFIX_ID` |
| [NMDP_SUBTYPE](NMDP_SUBTYPE.md) | `NMDP_SUFFIX_ID` |

