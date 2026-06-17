# CS_CPP_TIER_DETAIL

> Stores multiple values for categories applied to a ruleset (a ruleset (also called tier) is an organization of rules that get applied to a set of charges for an encounter). The categories that can be applied to the ruleset are organization, insurance organization, health plan, encounter type and fin class.

**Description:** Charge Services Charge Pre-Processor Tier Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CS_CPP_TIER_DETAIL_ENTITY_ID` | DOUBLE | NOT NULL |  | Will store corresponding values i.e. code values or id's |
| 3 | `CS_CPP_TIER_DETAIL_ENTITY_NAME` | VARCHAR(40) | NOT NULL |  | Will store the Entity Names. For example, "ORGANIZATION", "HEALTH_PLAN", "CODE_VALUE". |
| 4 | `CS_CPP_TIER_DETAIL_ID` | DOUBLE | NOT NULL |  | The unique primary key of this table. It is an internally generated number. |
| 5 | `CS_CPP_TIER_DETAIL_SUBTYPE` | VARCHAR(40) | NOT NULL |  | Identifies the type of tier detail associated to the Tier. Examples are encntr_type, insurance_org, encntr_type_class, and fin_class. |
| 6 | `CS_CPP_TIER_ID` | DOUBLE | NOT NULL | FK→ | Stores the ID of the Tier that the detail is associated to. It is a foreign key to the CS_CPP_TIER table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CS_CPP_TIER_ID` | [CS_CPP_TIER](CS_CPP_TIER.md) | `CS_CPP_TIER_ID` |

