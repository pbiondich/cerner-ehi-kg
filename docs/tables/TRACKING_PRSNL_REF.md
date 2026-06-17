# TRACKING_PRSNL_REF

> Tracking table used to define assigned references such as teams to each tracking personnel provider.

**Description:** Tracking Personnel Reference Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `TRACKING_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Tracking identifier of the provider that this reference is to be associated with. |
| 3 | `TRACKING_PRSNL_REF_ID` | DOUBLE | NOT NULL |  | Tracking Personnel Reference Identifier |
| 4 | `TRACKING_REF_ID` | DOUBLE | NOT NULL | FK→ | The associated tracking reference identifier used to define which team or other tracking reference is associated with this provider. |
| 5 | `TRACKING_REF_TYPE_CD` | DOUBLE | NOT NULL | FK→ | Tracking Reference Type Code used to identify the type of tracking reference being defined. This field is provided to quickly access all tracking personnel references that are of a desired reference type. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TRACKING_PRSNL_ID` | [TRACKING_PRSNL](TRACKING_PRSNL.md) | `TRACKING_PRSNL_ID` |
| `TRACKING_REF_ID` | [TRACK_REFERENCE](TRACK_REFERENCE.md) | `TRACKING_REF_ID` |
| `TRACKING_REF_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

