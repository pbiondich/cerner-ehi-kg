# PBS_INDICATION

> Australian Pharmaceutical Benefits Schedule - Stores links between PBS items and restrictions/indications for use

**Description:** PBS_INDICATION  
**Table type:** REFERENCE  
**Primary key:** `PBS_INDICATION_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `INDICATION_IDENT` | DOUBLE | NOT NULL |  | PBS xml indication id |
| 4 | `PBS_INDICATION_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the PBS_INDICATION table. It is an internal system assigned number. |
| 5 | `PBS_LISTING_ID` | DOUBLE | NOT NULL | FK→ | Foreign key from PBS_LISTING table |
| 6 | `RESTRICTION_TEXT` | LONGTEXT |  |  | Restriction Indication Text |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PBS_LISTING_ID` | [PBS_LISTING](PBS_LISTING.md) | `PBS_LISTING_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [PBS_AUTHORITY](PBS_AUTHORITY.md) | `PBS_INDICATION_ID` |

