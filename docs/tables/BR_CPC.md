# BR_CPC

> Group of Comprehensive Primary Care Eligible Providers

**Description:** Bedrock Comprehensive Primary Care  
**Table type:** REFERENCE  
**Primary key:** `BR_CPC_ID`  
**Columns:** 14  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CPC_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_CPC table. |
| 4 | `BR_CPC_NAME` | VARCHAR(255) | NOT NULL |  | Name string associated to the CPC |
| 5 | `CPC_SITE_ID_TXT` | VARCHAR(50) | NOT NULL |  | The site id is an 8 character alphanumeric value that is provided to the client from CMS for this new measure submission process. The site id begins with the two letter state code (OK, MO, etc.) followed by six numerals. The identifier is assigned to each practice site that is taking part in the CPC group measure submissions. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 8 | `ORIG_BR_CPC_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the original PK from BR_CPC. |
| 9 | `TAX_ID_NBR_TXT` | VARCHAR(50) | NOT NULL |  | Stores the CPC's tax id number. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_BR_CPC_ID` | [BR_CPC](BR_CPC.md) | `BR_CPC_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [BR_CPC](BR_CPC.md) | `ORIG_BR_CPC_ID` |
| [BR_CPC_ELIG_PROV_RELTN](BR_CPC_ELIG_PROV_RELTN.md) | `BR_CPC_ID` |
| [BR_CPC_LOC_RELTN](BR_CPC_LOC_RELTN.md) | `BR_CPC_ID` |
| [LH_BR_CPC_LOC_RELTN](LH_BR_CPC_LOC_RELTN.md) | `BR_CPC_ID` |
| [LH_QRDA_SETUP_DATA](LH_QRDA_SETUP_DATA.md) | `BR_CPC_ID` |

