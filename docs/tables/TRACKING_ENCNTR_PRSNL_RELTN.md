# TRACKING_ENCNTR_PRSNL_RELTN

> Tracking table used to cross-reference which personnel provider records are related to each encounter tracked.

**Description:** Tracking Encounter Personnel Relation Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ENCNTR_PRSNL_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Provider relationship identifier used to define the relationship of the provider to the encounter. |
| 3 | `ENCNTR_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking ID from the Tracking Item table used to identify the cross-reference identifier for the encounter being tracked. |
| 4 | `PRSNL_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | Tracking ID from the Tracking Item table used to identify the cross-reference identifier for the provider (person) being tracked. |
| 5 | `TRACKING_ENCNTR_PRSNL_RELTN_ID` | DOUBLE | NOT NULL |  | Unique tracking identifier used to define the cross-reference between the provider records and the associated encounters. |
| 6 | `TRACKING_ID` | DOUBLE | NOT NULL |  | Cross-reference tracking item identifier of the patient that is to be associated with a provider. |
| 7 | `TRACKING_LOCATOR_ID` | DOUBLE | NOT NULL | FK→ | Cross-reference tracking locator identifier of the provider location that is associated with a patient. |
| 8 | `TRACKING_PRSNL_ID` | DOUBLE | NOT NULL |  | Cross-reference tracking personnel identifier of the provider that is to be associated with a patient. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_PRSNL_RELTN_ID` | [ENCNTR_PRSNL_RELTN](ENCNTR_PRSNL_RELTN.md) | `ENCNTR_PRSNL_RELTN_ID` |
| `ENCNTR_TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |
| `PRSNL_TRACKING_ID` | [TRACKING_ITEM](TRACKING_ITEM.md) | `TRACKING_ID` |
| `TRACKING_LOCATOR_ID` | [TRACKING_LOCATOR](TRACKING_LOCATOR.md) | `TRACKING_LOCATOR_ID` |

