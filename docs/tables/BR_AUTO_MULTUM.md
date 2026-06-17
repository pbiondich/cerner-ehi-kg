# BR_AUTO_MULTUM

> Because not all the data in the Multum tables is correct, the br_auto_multum table provides corrected data for the items that need corrected data. If a Multum item exists on the the br_auto_multum table then the fields on this table will be used instead of the ones in the Multum table.

**Description:** Bedrock Auto Multum  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 31

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_NAME` | VARCHAR(255) |  |  | Brand name column |
| 2 | `CONCENTRATION_PER_ML` | DOUBLE |  |  | Concentration per ML field |
| 3 | `CONCENTRATION_UNIT` | VARCHAR(40) |  |  | Concentration display field |
| 4 | `CONCENTRATION_UNIT_CKI` | VARCHAR(255) |  |  | CKI field |
| 5 | `DC_DISPLAY_DAYS` | DOUBLE |  |  | Used to populate the dc_display_days field on the order_catalog table |
| 6 | `DC_INTER_DAYS` | DOUBLE |  |  | Used to populate the dc_inter_days field on the order_catalog table |
| 7 | `DEF_FORMAT` | DOUBLE |  |  | Order entry format flag |
| 8 | `DISPENSE_QTY` | DOUBLE |  |  | Dispense quantityconcetnration unit cki |
| 9 | `DISPENSE_QTY_UNIT` | VARCHAR(40) |  |  | Dispense quantity display field |
| 10 | `DISPENSE_QTY_UNIT_CKI` | VARCHAR(255) |  |  | Cki field |
| 11 | `DIVISIBLE_IND` | DOUBLE |  |  | Divisibility indicator |
| 12 | `GENERIC_NAME` | VARCHAR(255) |  |  | Generic name field |
| 13 | `INFINITE_DIV_IND` | DOUBLE |  |  | Infinite divisibility indicator |
| 14 | `LABEL_DESCRIPTION` | VARCHAR(255) |  |  | Label description field |
| 15 | `MINIMUM_DOSE_QTY` | DOUBLE |  |  | Minimum dose quantity field |
| 16 | `MMDC` | VARCHAR(25) | NOT NULL |  | Main Multum drug code |
| 17 | `PRODUCT_TYPE` | VARCHAR(6) |  |  | Valid values for type flag are CONC, PKGVOL, and STD |
| 18 | `SEARCH_CONT` | DOUBLE |  |  | Continuous filter indicator |
| 19 | `SEARCH_INTERMIT` | DOUBLE |  |  | Intermittent filter indicator |
| 20 | `SEARCH_MED` | DOUBLE |  |  | Medication filter indicator |
| 21 | `STRENGTH` | DOUBLE |  |  | dosage Strength |
| 22 | `STRENGTH_UNIT` | VARCHAR(40) |  |  | Strength display field |
| 23 | `STRENGTH_UNIT_CKI` | VARCHAR(255) |  |  | Cki field |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VOLUME` | DOUBLE |  |  | Volume field |
| 30 | `VOLUME_UNIT` | VARCHAR(40) |  |  | Volume display field |
| 31 | `VOLUME_UNIT_CKI` | VARCHAR(255) |  |  | Cki field |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

