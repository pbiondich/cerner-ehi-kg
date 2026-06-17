# BR_CPC_ELIG_PROV_RELTN

> Stores the relationship between CPCs and eligible providers.

**Description:** Bedrock Comprehensive Primary Care Eligible Provider Relation  
**Table type:** REFERENCE  
**Primary key:** `BR_CPC_ELIG_PROV_RELTN_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CPC_ELIG_PROV_RELTN_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the BR_CPC_ELIG_PROV_RELTN table. |
| 4 | `BR_CPC_ID` | DOUBLE | NOT NULL | FK→ | The CPC group that this eligible provider belongs to. |
| 5 | `BR_ELIGIBLE_PROVIDER_ID` | DOUBLE | NOT NULL | FK→ | The eligible provider that is a part of this CPC group. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `ORIG_BR_CPC_ELIG_PROV_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the original PK value for BR_CPC_ELIG_PROV_RELTN_ID |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BR_CPC_ID` | [BR_CPC](BR_CPC.md) | `BR_CPC_ID` |
| `BR_ELIGIBLE_PROVIDER_ID` | [BR_ELIGIBLE_PROVIDER](BR_ELIGIBLE_PROVIDER.md) | `BR_ELIGIBLE_PROVIDER_ID` |
| `ORIG_BR_CPC_ELIG_PROV_RELTN_ID` | [BR_CPC_ELIG_PROV_RELTN](BR_CPC_ELIG_PROV_RELTN.md) | `BR_CPC_ELIG_PROV_RELTN_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BR_CPC_ELIG_PROV_RELTN](BR_CPC_ELIG_PROV_RELTN.md) | `ORIG_BR_CPC_ELIG_PROV_RELTN_ID` |

