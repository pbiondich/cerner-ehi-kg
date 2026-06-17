# REGIMEN

> Storage for regimens patient is on.

**Description:** REGIMEN  
**Table type:** ACTIVITY  
**Primary key:** `REGIMEN_ID`  
**Columns:** 19  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. it is an internal system assigned number. |
| 2 | `END_DT_TM` | DATETIME |  |  | The regimen end date time |
| 3 | `END_TZ` | DOUBLE |  |  | TIME ZONE FOR THE END TIME |
| 4 | `ORDERED_AS_NAME` | VARCHAR(100) | NOT NULL |  | Regimen synonym name used when the regimen was added |
| 5 | `ORDER_DT_TM` | DATETIME |  |  | date and time the regimen was ordered |
| 6 | `ORDER_TZ` | DOUBLE |  |  | THE TIME ZONE FOR THE ORDER DATE/TIME |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. it is an internal system assigned number. |
| 8 | `REGIMEN_CATALOG_ID` | DOUBLE | NOT NULL | FK→ | sequence name: reference_seq Unique identifier for the REGIMEN_CATALOG table. Each change or revision made to a regimen creates a new regimen instance. |
| 9 | `REGIMEN_DESCRIPTION` | VARCHAR(1000) | NOT NULL |  | Regimen Name key of the field Regimen Name. This field has all capital letters and punctuation removed. It is used for indexing and searching for a regimen catalog. |
| 10 | `REGIMEN_ID` | DOUBLE | NOT NULL | PK | sequence name: CareNet_seq Unique identifier for the REGIMEN table. |
| 11 | `REGIMEN_NAME` | VARCHAR(100) | NOT NULL |  | REGIMEN_NAME refers to the display name for the regimen. |
| 12 | `REGIMEN_STATUS_CD` | DOUBLE | NOT NULL |  | Regimen Status |
| 13 | `REQUESTED_START_DT_TM` | DATETIME |  |  | Estimated Regimen start date and time. |
| 14 | `REQUESTED_START_TZ` | DOUBLE |  |  | TIME ZONE FOR THE REQUESTED START DATE/TIME |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REGIMEN_CATALOG_ID` | [REGIMEN_CATALOG](REGIMEN_CATALOG.md) | `REGIMEN_CATALOG_ID` |

## Referenced by (8)

| From table | Column |
|------------|--------|
| [PRECOMPONENT_ORDER_RELTN](PRECOMPONENT_ORDER_RELTN.md) | `REGIMEN_ID` |
| [REGIMEN_ACTION](REGIMEN_ACTION.md) | `REGIMEN_ID` |
| [REGIMEN_ATTRIBUTE](REGIMEN_ATTRIBUTE.md) | `REGIMEN_ID` |
| [REGIMEN_DETAIL](REGIMEN_DETAIL.md) | `REGIMEN_ID` |
| [REGIMEN_DETAIL_ACTION](REGIMEN_DETAIL_ACTION.md) | `REGIMEN_ID` |
| [REGIMEN_DETAIL_R](REGIMEN_DETAIL_R.md) | `REGIMEN_ID` |
| [REGIMEN_DOCUMENTATION](REGIMEN_DOCUMENTATION.md) | `REGIMEN_ID` |
| [UKR_SACT](UKR_SACT.md) | `REGIMEN_ID` |

