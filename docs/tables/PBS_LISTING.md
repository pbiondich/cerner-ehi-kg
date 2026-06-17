# PBS_LISTING

> Australian Pharmaceutical Benefits Schedule - information on the availability of PBS items.

**Description:** PBS_LISTING  
**Table type:** REFERENCE  
**Primary key:** `PBS_LISTING_ID`  
**Columns:** 19  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ATC_PRINT_OPTION` | VARCHAR(1) | NOT NULL |  | Determines how entry is printed in published PBS manual. 1 - print full entry only 2 - print full entry with cross ref 3 - print drug name only 4 - do not print |
| 2 | `DANGEROUS_DRUG_FEE_TXT` | VARCHAR(10) |  |  | Dangerous Drug Fee Indicator |
| 3 | `DISPENSE_FEE_TYPE_CODE` | VARCHAR(2) | NOT NULL |  | Dispense Fee Type Code. Additional fees based on dispense type. NF - No Fee RP - ready Prepared EP - extemp prepared EW - extemp + water |
| 4 | `DRUG_TYPE_MEAN` | VARCHAR(2) | NOT NULL |  | Drug type meaning |
| 5 | `INCREASE_MAXIMUM_QTY` | DOUBLE |  |  | Maximum Quantity increase limit |
| 6 | `INCREASE_NBR_OF_RPT` | DOUBLE |  |  | Number of Repeat increase limit |
| 7 | `MAXIMUM_QTY` | DOUBLE | NOT NULL |  | Maximum quantity approved for dispense. Whole number only |
| 8 | `MAXIMUM_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | Maximum quantity code related to MAXIMUM_QTY. Code Set 54 |
| 9 | `NUMBER_OF_RPT` | DOUBLE | NOT NULL |  | Maximum number of repeats/refills approved. Whole number only |
| 10 | `PBS_ATC_ID` | DOUBLE | NOT NULL |  | Foreign Key value from PBS_ATC table. Anatomic Therapeutic Class code. |
| 11 | `PBS_ITEM_CODE` | VARCHAR(5) | NOT NULL |  | PBS Code |
| 12 | `PBS_ITEM_IDENT` | VARCHAR(11) | NOT NULL |  | PBS Item XML reference ID |
| 13 | `PBS_LISTING_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PBS_LISTING table. It is an internal system assigned number. |
| 14 | `RESTRICTION_CODE` | VARCHAR(1) | NOT NULL |  | Restriction level U - Unrestricted R - Restricted A - Authority Required |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PBS_INDICATION](PBS_INDICATION.md) | `PBS_LISTING_ID` |
| [PBS_ITEM](PBS_ITEM.md) | `PBS_LISTING_ID` |
| [PBS_PRICING](PBS_PRICING.md) | `PBS_LISTING_ID` |

