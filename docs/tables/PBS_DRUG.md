# PBS_DRUG

> Australian Pharmaceutical Benefits Schedule - definition of generic drug forms and strengths.

**Description:** PBS_DRUG  
**Table type:** REFERENCE  
**Primary key:** `PBS_DRUG_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `BRAND_IDENT` | VARCHAR(45) | NOT NULL |  | Brand xml reference id |
| 3 | `BRAND_NAME` | VARCHAR(45) | NOT NULL |  | Brand Name. May be truncated at 45 char. |
| 4 | `DRUG_UUID` | VARCHAR(255) | NOT NULL |  | The drug unique universal identifier |
| 5 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 6 | `FORM_LEGAL` | VARCHAR(400) |  |  | Form Strength legal documentation |
| 7 | `FORM_PACK` | VARCHAR(100) |  |  | FORM PACK column |
| 8 | `FORM_STRENGTH` | VARCHAR(400) | NOT NULL |  | Form Strength. Concatenated form and strength, may be truncated at 150 char. |
| 9 | `PACK_SIZE` | DOUBLE | NOT NULL |  | Quantity contained in manufacturer's package |
| 10 | `PACK_SIZE_UNIT_CD` | DOUBLE | NOT NULL |  | Pack size code related to pack_size_item. code set 54 |
| 11 | `PBS_DRUG_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PBS_DRUG table. It is an internal system assigned number. |
| 12 | `PBS_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign Key PBS_ITEM |
| 13 | `PBS_MANUFACTURER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key PBS_MANF |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PBS_ITEM_ID` | [PBS_ITEM](PBS_ITEM.md) | `PBS_ITEM_ID` |
| `PBS_MANUFACTURER_ID` | [PBS_MANF](PBS_MANF.md) | `PBS_MANUFACTURER_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PBS_OCS_MAPPING](PBS_OCS_MAPPING.md) | `PBS_DRUG_ID` |

