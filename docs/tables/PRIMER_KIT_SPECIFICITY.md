# PRIMER_KIT_SPECIFICITY

> Defines a specific allele and specificity for which an HLA molecular testing primer kit will be used to test for.

**Description:** Primer Kit Specificity  
**Table type:** REFERENCE  
**Primary key:** `ALLELE_CD`, `LOT_NUMBER_ID`  
**Columns:** 8  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLELE_CD` | DOUBLE | NOT NULL | PK | The code for an allele which this Aliquotted Primer Kit tests for. |
| 2 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK FK→ | Relates the Aliquotted Primer Kit allele to the inventory lot and related map. It is a foreign key reference to the primary key of the lot_number_info table. |
| 3 | `SPECIFICITY_CD` | DOUBLE | NOT NULL |  | The code for the specificity of the allele this Aliquotted Primer Kit tests for. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [ALIQUOTTED_PRIMER_KIT](ALIQUOTTED_PRIMER_KIT.md) | `LOT_NUMBER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [POSITIVE_TUBES](POSITIVE_TUBES.md) | `ALLELE_CD` |
| [POSITIVE_TUBES](POSITIVE_TUBES.md) | `LOT_NUMBER_ID` |

