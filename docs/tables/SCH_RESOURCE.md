# SCH_RESOURCE

> A resource is an item of limited availability whose usage is managed.

**Description:** Scheduling Resource  
**Table type:** REFERENCE  
**Primary key:** `RESOURCE_CD`  
**Columns:** 31  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CANDIDATE_ID` | DOUBLE | NOT NULL |  | A sequence-generated number to uniquely identify the specific row in the database. |
| 7 | `DESCRIPTION` | VARCHAR(255) |  |  | A long description used for documentation. |
| 8 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 9 | `INFO_SCH_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the information-only text associated with the record. |
| 10 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for the inventory item. |
| 11 | `ITEM_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location identifier associated with the inventory item type. |
| 12 | `LOGICAL_DOMAIN_ID` | DOUBLE | NOT NULL | FK→ | The unique identifier for a logical domain. This identifier allows the data to be grouped by logical domain. For example, If you assign clients a logical_domain_id this would allow you to store data for multiple clients on this table. |
| 13 | `MNEMONIC` | VARCHAR(100) | NOT NULL |  | A 100-character string used for identification and selection. |
| 14 | `MNEMONIC_KEY` | VARCHAR(100) | NOT NULL |  | The MNEMONIC in uppercase with the non-alphanumeric characters removed. |
| 15 | `MNEMONIC_KEY_A_NLS` | VARCHAR(400) |  |  | A native sort version of the MNEMONIC_KEY FIELD. |
| 16 | `MNEMONIC_KEY_NLS` | VARCHAR(202) |  |  | A native sort version of the MNEMONIC_KEY FIELD. Obsolete column, replaced by MNEMONIC_KEY_A_NLS. |
| 17 | `NULL_DT_TM` | DATETIME | NOT NULL |  | contains 31-DEC-2100 00:00:00.00. This field is used to maintain foreign keys to tables that contain a VERSION_DT_TM in the primary key. |
| 18 | `OWNER_ORG_ID` | DOUBLE | NOT NULL | FK→ | ID of the organization that owns this resource, used to determine unique service names per service providing organization |
| 19 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the prsnl table. It is an internal system assigned number. |
| 20 | `QUOTA` | DOUBLE | NOT NULL |  | The booking limit. |
| 21 | `RESOURCE_CD` | DOUBLE | NOT NULL | PK FK→ | The identifier for the resource. A resource is an item of limited availability. |
| 22 | `RES_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines if the resource is associated external objects (i.e. person, service_resource, etc.) 1 - General Resource, 2 - Personnel Resource, 3- Service Resource |
| 23 | `SCH_SERVICE_ID` | DOUBLE | NOT NULL |  | ** OBSOLETE COLUMN (Parent table is obsolete) ** Foreign key to table SCH_Service (Parent table) |
| 24 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The generic term used to denote a physical place in the Health Care Organization. |
| 25 | `SURGICAL_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of surgical resource. 0 - Not a surgeon. 1 indicates the resource is a SURGEON. |
| 26 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 29 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 30 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `VERSION_DT_TM` | DATETIME | NOT NULL |  | The version date and time marks the date the record became historical. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INFO_SCH_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `ITEM_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOGICAL_DOMAIN_ID` | [LOGICAL_DOMAIN](LOGICAL_DOMAIN.md) | `LOGICAL_DOMAIN_ID` |
| `OWNER_ORG_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RESOURCE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [MP_AMB_ORG_SAT](MP_AMB_ORG_SAT.md) | `RESOURCE_CD` |
| [SCH_APPT_TYPE](SCH_APPT_TYPE.md) | `GRP_RESOURCE_CD` |
| [SCH_CAB_WORKGROUP_RES](SCH_CAB_WORKGROUP_RES.md) | `RESOURCE_CD` |
| [SCH_DATE_APPLY](SCH_DATE_APPLY.md) | `RESOURCE_CD` |
| [SCH_EVENT_RECUR_ROLE](SCH_EVENT_RECUR_ROLE.md) | `RESOURCE_CD` |
| [SCH_EVENT_RECUR_ROLE](SCH_EVENT_RECUR_ROLE.md) | `SERVICE_RESOURCE_CD` |
| [SCH_RESOURCE_LOCK](SCH_RESOURCE_LOCK.md) | `RESOURCE_CD` |

