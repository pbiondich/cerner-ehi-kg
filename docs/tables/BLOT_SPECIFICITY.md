# BLOT_SPECIFICITY

> Defines a specific allele and specificity for which an HLA molecular testing blot will be used to test for.

**Description:** Blot Specificity  
**Table type:** REFERENCE  
**Primary key:** `ALLELE_CD`, `LOT_NUMBER_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ALLELE_CD` | DOUBLE | NOT NULL | PK | The code for an allele which this Molecular Blot tests for. |
| 2 | `LOCI_CD` | DOUBLE |  |  | The code for a specific HLA Loci that the Molecular Blot tests for. |
| 3 | `LOT_NUMBER_ID` | DOUBLE | NOT NULL | PK FK→ | Relates the molecular blot allele to the inventory lot and related blot. It is a foreign key reference to the primary key of the lot_number_info table. |
| 4 | `SPECIFICITY_CD` | DOUBLE |  |  | The code for an specificity which this Molecular Blot tests for. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOT_NUMBER_ID` | [MOLECULAR_BLOT](MOLECULAR_BLOT.md) | `LOT_NUMBER_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [POSITIVE_PROBES](POSITIVE_PROBES.md) | `ALLELE_CD` |
| [POSITIVE_PROBES](POSITIVE_PROBES.md) | `LOT_NUMBER_ID` |

