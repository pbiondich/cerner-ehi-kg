# BR_CCN

> Stores information about CMS Certification Numbers, which are unique identifiers given to hospitals by the Centers for Medicare and Medicaid Services that identify the site that is submitting data to them.

**Description:** Bedrock CMS Certification Number  
**Table type:** REFERENCE  
**Primary key:** `BR_CCN_ID`  
**Columns:** 15  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CCN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_CCN table. |
| 4 | `CCN_NAME` | VARCHAR(150) | NOT NULL |  | Stores the name associated to the CCN. |
| 5 | `CCN_NBR` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 6 | `CCN_NBR_TXT` | VARCHAR(150) | NOT NULL |  | Stores the CCN's identifying number. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 9 | `ORIG_BR_CCN_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. The original BR_CCN_ID value. |
| 10 | `TAX_ID_NBR_TXT` | VARCHAR(50) | NOT NULL |  | Stores the tax id number associated to the CCN. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `ORIG_BR_CCN_ID` | [BR_CCN](BR_CCN.md) | `BR_CCN_ID` |

## Referenced by (4)

| From table | Column |
|------------|--------|
| [BR_CCN](BR_CCN.md) | `ORIG_BR_CCN_ID` |
| [BR_CCN_EXTENSION](BR_CCN_EXTENSION.md) | `BR_CCN_ID` |
| [BR_CCN_LOC_RELTN](BR_CCN_LOC_RELTN.md) | `BR_CCN_ID` |
| [BR_PRSNL_CCN_RELTN](BR_PRSNL_CCN_RELTN.md) | `BR_CCN_ID` |

