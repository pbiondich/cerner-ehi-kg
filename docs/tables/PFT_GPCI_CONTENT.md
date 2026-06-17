# PFT_GPCI_CONTENT

> Stores information from the CMS Geographic Practice Cost Index Fileliability insurance (PLI). Three distinct GPCIs are used to calculate the payment schedule amount for a service in a Medicare locality.

**Description:** ProFit Geographic Practice Cost Index Content  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LOCALITY_CODE_TXT` | VARCHAR(2) |  |  | Locality code assigned by CMS |
| 5 | `LOCALITY_NAME_TXT` | VARCHAR(50) |  |  | Name of locality assigned by CMS |
| 6 | `MALPRACTICE_GPCI_NBR` | DOUBLE |  |  | Malpractice related geographic practice cost index component |
| 7 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Identifies the insurance organization that corresponds to the given carrier number organization alias |
| 8 | `PFT_GPCI_CONTENT_ID` | DOUBLE | NOT NULL |  | Unique identifier for GPCI Content record |
| 9 | `PRACTICE_GPCI_NBR` | DOUBLE |  |  | Practice related geographic practice cost index component |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `WORK_GPCI_NBR` | DOUBLE |  |  | Work related geographic practice cost index component |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

