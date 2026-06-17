# PBS_ITEM

> Australian Pharmaceutical Benefits Schedule - definition of a generic drug

**Description:** PBS_ITEM  
**Table type:** REFERENCE  
**Primary key:** `PBS_ITEM_ID`  
**Columns:** 15  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CAUTION_FLAG` | DOUBLE | NOT NULL |  | Drug has cautionary information. 1 - Caution attached, 0 - Otherwise |
| 3 | `DRUG_NAME` | VARCHAR(200) | NOT NULL |  | Drug Name. May be truncated at 200 char. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `NBR_OF_DAYS_BETWEEN_REFILLS` | DOUBLE | NOT NULL |  | Number of days between refills for SN20DR rule |
| 6 | `NOTE_FLAG` | DOUBLE | NOT NULL |  | Drug has additional notes attached. 1 - note attached, 0 - otherwise |
| 7 | `PBS_ITEM_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PBS_ITEM table. It is an internal system assigned number. |
| 8 | `PBS_ITEM_IDENT` | VARCHAR(11) | NOT NULL |  | PBS Item XML reference id |
| 9 | `PBS_LISTING_ID` | DOUBLE | NOT NULL | FK→ | Foreign key PBS_LISTING |
| 10 | `SN20DR_IND` | DOUBLE | NOT NULL |  | Indicates if the SN20DR rule applies to the PBS item code |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PBS_LISTING_ID` | [PBS_LISTING](PBS_LISTING.md) | `PBS_LISTING_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PBS_CAUTION_RELTN](PBS_CAUTION_RELTN.md) | `PBS_ITEM_ID` |
| [PBS_DRUG](PBS_DRUG.md) | `PBS_ITEM_ID` |
| [PBS_NOTE_RELTN](PBS_NOTE_RELTN.md) | `PBS_ITEM_ID` |

